from datetime import datetime
from typing import Optional, List

from pydantic import validator, BaseModel
from API.database import get_connection

class Patients(BaseModel):
    id: str
    clinical_information: dict
    created_at: Optional[datetime] = None

    @staticmethod
    def save(patients):
        """
            Saves user to database.
        """

        patients_dict = patients.dict()
        patients_dict["samples"] = []
        database = get_connection()
        database.patients.insert_one(patients_dict)

        return patients_dict
