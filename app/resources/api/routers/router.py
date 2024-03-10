# -- mio
from fastapi import APIRouter
#from app.resources.api.routers.rutas_app import router as resources_router

rutas = APIRouter()
#router.include_router(resources_router, prefix="/example_api", tags=["example_api"])

@rutas.get('/okok')
async def ok():
    return "ok"