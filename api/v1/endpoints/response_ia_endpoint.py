#Endpoint of response AI

from typing import  Optional
from core.config import settings
from fastapi import UploadFile, File, APIRouter, status
from models.database.registry_db import RegistryAI
from services.ai_huggingface.prompt import PromptIA
from services.ai_huggingface.api_hugginface import HuggingfaceIA
from services.xlsx_data.read_xlsx import FileXlsx
from schemas.ai_schema import AiSchema

router = APIRouter()

@router.post('/send', status_code=status.HTTP_201_CREATED, response_model=AiSchema)

async def send_file(file: UploadFile = File()) -> Optional[AiSchema, dict]:
    """
    Specific endpoint for send file AI

    :param file: file for upload

    :return: object AiSchema
    """

    file_xlsx = FileXlsx(file_name=file.filename)

    file_name = file_xlsx.file_name

    checker = file_xlsx.extension_check()

    if type(checker) == dict:
        RegistryAI.insert_registry_ia(
            file_name=file_name,
            extension_file_name='Desconhecido',
            url_ia=settings.hugginface_api_url,
            status='OK',
            status_api='201',
            error_api=str(checker.get('file')),
        )

        return checker

    contents = await file.read()

    dataframe = file_xlsx.read_xlsx_file(file=contents)

    data = file_xlsx.convert_to_text(file=dataframe)

    prompt = PromptIA(data_text=data)

    ia = HuggingfaceIA(huggingface_url=settings.hugginface_api_url, token=settings.hugginface_token)

    payload = ia.create_payload(prompt=prompt.prompt)

    result = ia.send_api_huggingface(payload=payload)

    if result['analise']:

        RegistryAI.insert_registry_ia(
            file_name=file_name,
            extension_file_name='xlsx',
            url_ia=settings.hugginface_api_url,
            prompt_ia=prompt.prompt,
            status='OK',
            status_api='201',
            ai_text_success=str(result.get('analise'))
        )

    else:

        RegistryAI.insert_registry_ia(
            file_name=file_name,
            extension_file_name='xlsx',
            url_ia=settings.hugginface_api_url,
            prompt_ia=prompt.prompt,
            status='ERROR',
            status_api='201',
            ai_error=str(result.get('error'))

        )
