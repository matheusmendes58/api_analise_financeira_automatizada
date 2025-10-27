# Main APP

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError, ArgumentError
from api.v1.router_api import api_router
from core.config import settings
from custom_exception.db_exceptions import StringConnection, CredentialsErrorConnection
from models.database.base import create_all

app = FastAPI(
    title='Automated Financial Analysis API',
    description='This API consumes an excel file and makes a call to AI to perform an analysis.',
    version='1.0.0',
    contact={
        'name': 'Matheus Mendes Santos',
    },
    docs_url="/documentation",        # Swagger UI
    redoc_url="/redoc-custom",       # ReDoc
    openapi_url="/openapi.json"      # JSON do schema
)
app.include_router(api_router, prefix=settings.api_v1_str)

@app.middleware("http")
async def google_error_handler(request: Request, call_next):
    """
    Capture error 500 in API

    :param request: Object Fastapi
    :param call_next: This function callback from FastAPI

    :return:
    """

    try:
        return await call_next(request)
    except Exception:
        if request.url.path.startswith(f"{settings.api_v1_str}/google"):
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "detail": "Google Gemini Service"
                }
            )

        raise

@app.middleware("http")
async def cohere_error_handler(request: Request, call_next):
    """
        Capture error 500 in API

        :param request: Object Fastapi
        :param call_next: This function callback from FastAPI

        :return:
        """

    try:
        return await call_next(request)
    except Exception:
        if request.url.path.startswith(f"{settings.api_v1_str}/cohere"):
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "detail": "Cohere Service"
                }
            )

        raise

if __name__ == '__main__':
    import uvicorn

    try:
        create_all()

    except OperationalError:
        raise CredentialsErrorConnection()

    except ArgumentError:
        raise StringConnection()

    except Exception as e:
        raise 'Unknown error'

    uvicorn.run('main:app', port=8000, log_level='info')
