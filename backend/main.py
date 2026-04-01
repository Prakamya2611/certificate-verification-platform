from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import hashlib

app = FastAPI()

# ---------------- CORS FIX ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- STORAGE ----------------
issued_certificates = {}

class Certificate(BaseModel):
    student_name: str
    course_name: str
    issuer: str

# ---------------- ISSUE ----------------
@app.post("/certificates/issue")
def issue_certificate(data: Certificate):
    raw = f"{data.student_name}{data.course_name}{data.issuer}"
    cert_hash = hashlib.sha256(raw.encode()).hexdigest()

    issued_certificates[cert_hash] = {
        "student_name": data.student_name,
        "course_name": data.course_name,
        "issuer": data.issuer
    }

    return {
        "message": "Certificate issued",
        "certificate_hash": cert_hash
    }

# ---------------- VERIFY ----------------
@app.get("/certificates/verify/{cert_hash}")
def verify_certificate(cert_hash: str):
    if cert_hash in issued_certificates:
        return {
            "status": "VALID",
            "certificate": issued_certificates[cert_hash]
        }
    else:
        return {
            "status": "NOT VALID"
        }

@app.get("/")
def root():
    return {"message": "Certificate Platform Running"}
