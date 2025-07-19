from pydantic import BaseModel
from typing import Optional


class UploadPng(BaseModel):
    filename: str
    size: int
    target_printer_ip: str
    printed: bool
    error: Optional[str] = None
