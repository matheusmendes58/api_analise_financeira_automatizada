#Endpoint of response AI

from core.config import settings
from fastapi import UploadFile, File, APIRouter, status
from models.database.registry_db import RegistryAI
from services.ai_prompts.prompt import PromptIA
from services.ai_huggingface.api_hugginface import HuggingfaceIA
from services.xlsx_data.read_xlsx import FileXlsx
from utils.enum_status import StatusDbEnum, StatusApiEnum

router = APIRouter()

@router.post('/send',
             status_code=status.HTTP_201_CREATED,
             response_model=dict,
             summary='Send a file',
             description='Sends a file to the AI to perform a financial analysis '
                         'and provide a response from this analysis.',
             response_description='A dict with response from AI'
             )

async def send_file(file: UploadFile = File()) -> dict:
    """
    Specific endpoint for send file AI

    :param file: file for upload

    :return: object AiSchema
    """

    return {'response': 'This endpoint is disabled use another service'}

    # file_xlsx = FileXlsx(file_name=file.filename)
    #
    # file_name = file_xlsx.file_name
    #
    # checker = file_xlsx.extension_check()
    #
    # if type(checker) == dict:
    #     RegistryAI.insert_registry_ia(
    #         file_name=file_name,
    #         extension_file_name=StatusDbEnum.extension_file_name_error.value,
    #         url_ia=settings.hugginface_api_url,
    #         status=StatusDbEnum.error_db.value,
    #         status_api=StatusApiEnum.status_error_422.value,
    #         error_api=str(checker.get('file')),
    #     )
    #
    #     return checker
    #
    # contents = await file.read()
    #
    # dataframe = file_xlsx.read_xlsx_file(file=contents)
    #
    # data = file_xlsx.convert_to_text(file=dataframe)
    #
    # prompt = PromptIA(data_text=data)
    #
    # ia = HuggingfaceIA(huggingface_url=settings.hugginface_api_url, token=settings.hugginface_token)
    #
    # payload = ia.create_payload(prompt=prompt.prompt_huggingface)
    #
    # result = ia.send_api_huggingface(payload=payload)
    #
    # if result.get('analise'):
    #
    #     RegistryAI.insert_registry_ia(
    #         file_name=file_name,
    #         extension_file_name=StatusDbEnum.extension_file_name_ok.value,
    #         url_ia=settings.hugginface_api_url,
    #         prompt_ia=prompt.prompt_huggingface,
    #         status=StatusDbEnum.ok_db.value,
    #         status_api=StatusApiEnum.status_ok_201.value,
    #         ai_text_success=str(result.get('analise'))
    #     )
    #
    # else:
    #
    #     RegistryAI.insert_registry_ia(
    #         file_name=file_name,
    #         extension_file_name=StatusDbEnum.extension_file_name_ok.value,
    #         url_ia=settings.hugginface_api_url,
    #         prompt_ia=prompt.prompt_huggingface,
    #         status=StatusDbEnum.error_db.value,
    #         status_api=StatusApiEnum.status_error_400.value,
    #         ai_error=str(result.get('detalhes'))
    #     )
    #
    #     return result
