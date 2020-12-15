import uuid
from API.database import get_connection
from datetime import datetime
from typing import Optional, List
from pydantic import validator, BaseModel


class Patients(BaseModel):
    id: str
    clinical_information: dict
    created_at: Optional[datetime] = None


def new_patient(patient_data: dict) -> Patients:
    """
    Creates a new patient.
    """
    database = get_connection()
    patient = Patients(id=str(uuid.uuid4()), created_at=datetime.now(), clinical_information=patient_data)
    database.patients.insert(
        {
            "patient_data": patient.dict(exclude_unset=True)
        }
    )
    return patient


def see_all():
    """
        Search Patients by id
    """
    database = get_connection()
    patients_in_db = []
    patient: dict = database.patients.find()
    for p in patient:
        pat = p["patient_data"]
        patients_in_db.append(pat)
    print(patients_in_db)
    return patients_in_db


def delete(id_patient: str):
    """
        Delete patients by id
    """
    database = get_connection()
    col = database.patients
    query = {"patient_data.id": id_patient}
    col.delete_one(query)
