from fastapi import FastAPI, File, UploadFile, HTTPException, Header
from escpos.printer import Network
import tempfile


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI project is set up."}


@app.post("/upload")
async def upload_png(
    target_printer_ip: str = Header(...), file: UploadFile = File(...)
):
    if not target_printer_ip:
        raise HTTPException(status_code=400, detail="Target-Printer-IP header missing.")
    if file.content_type != "image/png":
        raise HTTPException(status_code=400, detail="Only PNG images are accepted.")
    content = await file.read()

    # Save the PNG temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    # Print using ESC/POS
    try:
        printer = Network(target_printer_ip)
        printer.image(tmp_path)
        printer.cut(feed=False, mode="PART")
        printed = True
    except Exception as e:
        printed = False
        error = str(e)

    return {
        "filename": file.filename,
        "size": len(content),
        "target_printer_ip": target_printer_ip,
        "printed": printed,
        **({"error": error} if not printed else {}),
    }
