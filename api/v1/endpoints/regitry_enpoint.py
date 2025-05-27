#Endpoint focused on software auditing

from typing import List, Union
from fastapi import APIRouter, status
from models.database.registry_db import RegistryAI
from schemas.ai_schema import AiSchema

router = APIRouter()

@router.get('/registry', status_code=status.HTTP_200_OK, response_model=List[AiSchema])

async def get_all_registry() -> Union[list, dict]:
    """
    Specific endpoint to bring all records from the database

    :return: A list records from database
    """

    records = RegistryAI.select_all_registry()

    if not records:
        return {'msg': 'No records found'}

    return records

@router.get('/registry/last', status_code=status.HTTP_200_OK, response_model=AiSchema)

async def get_last_registry() -> dict:
    """
    Specific endpoint to bring last record in database

    :return: a dict
    """

    record = RegistryAI.select_last_registry_in_table()

    if not record:
        return {'mgs': 'No record found'}

    return record
