from fastapi import FastAPI,Query
from routers.rutas_app import rutas

app =FastAPI()
app.include_router(rutas)

