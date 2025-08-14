#Endpoint of response AI
#TODO testar erro de api
#TODO Registrar erro em database
from core.config import settings
from fastapi import UploadFile, File, APIRouter, status
from models.database.registry_db import RegistryAI
from services.ai_prompts.prompt import PromptIA
from services.ai_cohere.chat_cohere import AiCohereChat
from services.xlsx_data.read_xlsx import FileXlsx

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

    file_xlsx = FileXlsx(file_name=file.filename)

    file_name = file_xlsx.file_name

    checker = file_xlsx.extension_check()

    if type(checker) == dict:
        RegistryAI.insert_registry_ia(
            file_name=file_name,
            extension_file_name='Unknown',
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

    ia = AiCohereChat(token=settings.cohere_token)

    result = ia.chat_cohere(prompt=prompt.prompt_cohere)

    RegistryAI.insert_registry_ia(
        file_name=file_name,
        extension_file_name='xlsx',
        url_ia='COHERE',
        prompt_ia=prompt.prompt_cohere,
        status='OK',
        status_api='201',
        ai_text_success=str(result))
