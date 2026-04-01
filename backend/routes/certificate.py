from fastapi import APIRouter
from pydantic import BaseModel
import hashlib

router = APIRouter(prefix="/certificates", tags=["Certificates"])

class Certificate(BaseModel):
    student_name: str
    course_name: str
    issuer: str

@router.post("/issue")
def issue_certificate(data: Certificate):
    raw_data = f"{data.student_name}{data.course_name}{data.issuer}"
    cert_hash = hashlib.sha256(raw_data.encode()).hexdigest()

    return {
        "message": "Certificate issued successfully",
        "certificate_hash": cert_hash
    }
