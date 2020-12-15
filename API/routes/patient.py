from fastapi import APIRouter, Depends, HTTPException, FastAPI, UploadFile, File
from pydantic import ValidationError

from API.logger import logger
from API.model.patient_model import Patients
from API.model.patient_model import *

router = APIRouter()


@router.post("/create", name="Create a new patient", tags=["patient"])
async def register(patient: dict) -> Patients:
    try:
        patient = new_patient(patient)
    except ValidationError as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=f"Patient could not be created")
    except Exception as e:
        logger.exception(e)

    return patient


@router.get("/all", name="Get patients of current clinician", tags=["patient"])
async def patients():
    patient = see_all()
    return patient


@router.delete(
    "/delete/{id_patient}", name="Delete patient by patient_id and clinic_id", tags=["patient"]
)
async def delete_patient(id_patient: str):
    try:
        patient = delete(id_patient)
        logger.debug(patient)
    except ValidationError as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=f"Patient could not be deleted")
    except Exception as e:
        logger.exception(e)
