#Routes to api

from fastapi import APIRouter
from api.v1.endpoints import huggingface_ai_endpoint
from api.v1.endpoints import cohere_ai_endpoint
from api.v1.endpoints import regitry_enpoint

api_router = APIRouter()
api_router.include_router(huggingface_ai_endpoint.router, prefix='/hugg', tags=['huggingface'])
api_router.include_router(cohere_ai_endpoint.router, prefix='/cohere', tags=['cohere'])
api_router.include_router(regitry_enpoint.router, prefix='/records', tags=['registry'])
