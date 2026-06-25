from app.schemas.patient import Patient


def validate_patient(patient: Patient):

    errors = []
    warnings = []

    if patient.resourceType != "Patient":
        errors.append("resourceType must be Patient")

    if not patient.name:
        errors.append("Patient name is required")

    if not patient.birthDate:
        errors.append("birthDate is required")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }