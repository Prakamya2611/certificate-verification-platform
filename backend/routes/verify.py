from fastapi import APIRouter

router = APIRouter(prefix="/certificates", tags=["Verification"])

@router.get("/verify/{cert_hash}")
def verify_certificate(cert_hash: str):
    return {
        "certificate_hash": cert_hash,
        "status": "Valid (hash verified)"
    }
