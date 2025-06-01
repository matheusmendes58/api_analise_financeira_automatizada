#Routes to api

from fastapi import APIRouter
from api.v1.endpoints import response_ia_endpoint
from api.v1.endpoints import regitry_enpoint

api_router = APIRouter()
api_router.include_router(response_ia_endpoint.router, prefix='/ai', tags=['ai'])
api_router.include_router(regitry_enpoint.router, prefix='/records', tags=['registry'])
