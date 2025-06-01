# Main APP

from fastapi import FastAPI
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
