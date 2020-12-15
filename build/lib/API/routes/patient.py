from typing import List

from fastapi import APIRouter, Depends, HTTPException, FastAPI, UploadFile, File
from pydantic import ValidationError

from ejemplo_4.logger import logger
from ejemplo_4.model.patients import Patients
from ejemplo_4.model.patient import Patient

router = APIRouter()

@router.post("/create", name="Create a new patient", tags=["patient"])
async def register(patient: dict) -> Patients:
    try:
        patient = Patient.new_patient(patient)
    except ValidationError as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=f"Patient could not be created")
    except Exception as e:
        logger.exception(e)

    return patient

@router.get("/all", name="Get patients of current clinician", tags=["patient"])
async def patients():
    patients = []
    patient = Patient.see_all(0)
    return patient

@router.delete(
    "/delete/{id_patient}", name="Delete patient by patient_id and clinic_id", tags=["patient"]
)
async def delete_patient(id_patient:str):
    try:
        patient = Patient.delete(id_patient)
        logger.debug(patient)
    except ValidationError as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=f"Patient could not be deleted")
    except Exception as e:
        logger.exception(e)
