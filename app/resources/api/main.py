from fastapi import FastAPI,Query
from routers.rutas_app import rutas
# rutas api
app =FastAPI()
app.include_router(rutas)

