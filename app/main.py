from typing_extensions import Annotated
from fastapi import Depends, FastAPI, APIRouter, File, UploadFile, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from escpos.printer import Network, Dummy
import tempfile
from pydantic import BaseModel
from typing import Optional


from fastapi import Body


class UploadPng(BaseModel):
    filename: str
    size: int
    target_printer_ip: str
    printed: bool
    error: Optional[str] = None


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "http://127.0.0.1",
        "https://hekaya.elnotah.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_printer(target_printer_ip: str = Header(...)):
    printer_profile = {
        "media": {
            "width": {
                "pixel": 576  # 72mm printable area for Xprinter Q807K
            }
        }
    }
    printer = Network(target_printer_ip)
    try:
        yield printer
    finally:
        printer.close()

PrinterDependency = Annotated[Network, Depends(get_printer)]
router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello, FastAPI project is set up."}


@router.post("/upload", response_model=UploadPng)
async def upload_png(
    #target_printer_ip: str = Header(...),
    printer: PrinterDependency,
    file: UploadFile = File(...),
   
) -> UploadPng:
    # if not target_printer_ip:
    #     raise HTTPException(status_code=400, detail="Target-Printer-IP header missing.")
    if file.content_type != "image/png":
        raise HTTPException(status_code=400, detail="Only PNG images are accepted.")
    content = await file.read()

    # Save the PNG temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    # Print using ESC/POS
    try:
        d = Dummy()
        d.image(tmp_path)
        d.cut()
        printer._raw(d.output)
      
        printed = True
    except Exception as e:
        printed = False
        error = str(e)

    return {
        "filename": file.filename,
        "size": len(content),
        "target_printer_ip": "192.168.1.64",  # Use the printer's host from the dependency
        "printed": printed,
        **({"error": error} if not printed else {}),
    }


# @router.post("/print-png-directly", response_model=UploadPng)
# async def print_png_directly(
#     target_printer_ip: str = Header(...),
#     file: UploadFile = File(...),
# ) -> UploadPng:
#     if not target_printer_ip:
#         raise HTTPException(status_code=400, detail="Target-Printer-IP header missing.")
#     if file.content_type != "image/png":
#         raise HTTPException(status_code=400, detail="Only PNG images are accepted.")
#     content = await file.read()

#     # Save the PNG temporarily
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
#         tmp.write(content)
#         tmp_path = tmp.name

#     # Print using ESC/POS
#     try:
#         printer = Network(target_printer_ip)
#         printer.image(tmp_path)
#         printer.cut()
#         printed = True
#     except Exception as e:
#         printed = False
#         error = str(e)

#     return {
#         "filename": file.filename,
#         "size": len(content),
#         "target_printer_ip": target_printer_ip,
#         "printed": printed,
#         **({"error": error} if not printed else {}),
#     }


# @router.post("/print-bytes")
# async def print_bytes(data: bytes = Body(...), target_printer_ip: str = Header(...)):
#     try:
#         printer = Network(target_printer_ip)
#         printer._raw(data)
#         printer.cut()
#         return {"printed": True}
#     except Exception as e:
#         return {"printed": False, "error": str(e)}


app.include_router(router, prefix="/pos-printers")
