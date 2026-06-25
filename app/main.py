from fastapi import FastAPI

from app.schemas.patient import Patient
from app.services.validator import validate_patient

app = FastAPI(
    title="FHIR Patient Validator",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FHIR Patient Validator"
    }


@app.post("/validate")
def validate(patient: Patient):
    return validate_patient(patient)