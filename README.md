# FHIR Patient Validator

A simple FastAPI-based service to validate FHIR Patient resources according to basic rules.

## Project purpose

This project provides a lightweight API that validates a FHIR Patient JSON object and returns:
- validation status
- errors
- warnings (reserved for future rules)

It is designed as a learning project for:
- FastAPI
- Pydantic models
- basic validation logic
- Git/GitHub workflows

---

## Features

- Validate FHIR Patient resources
- Check required fields (resourceType, name, birthDate)
- Structured validation response
- FastAPI automatic documentation (Swagger)

---

## Tech stack

- Python 3.12+
- FastAPI
- Pydantic
- Uvicorn
- Pytest

---

## Project structure

```
app/
schemas/        # Pydantic models
services/       # Validation logic
main.py         # FastAPI entry point
tests/          # Unit tests
examples/       # Sample JSON payloads
```

---

## Installation

```bash
git clone https://github.com/your-username/fhir-patient-validator.git
cd fhir-patient-validator

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```
---

## Run the project
```bash
uvicorn app.main:app --reload
```
Then open:
```bash
http://127.0.0.1:8000/docs
```
---

## API usage

Validate patient

POST /validate

Example payload:
```JSON
{
  "resourceType": "Patient",
  "id": "123",
  "name": [
    {
      "family": "Rossi",
      "given": ["Mario"]
    }
  ],
  "gender": "male",
  "birthDate": "1990-01-01"
}
```
Response

```JSON

{
  "valid": true,
  "errors": [],
  "warnings": []
}
```
--- 

## Tests

Run tests with: 
```bash
pytest
```
---

## Future improvements
```
full FHIR validation (HL7 standard compliance)
more detailed error reporting
support for multiple resource types
authentication layer
database integration
```
---
## Author
Benedetta Stef