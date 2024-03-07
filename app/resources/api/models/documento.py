from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# --------------------------------- Creacion de Tipos
class tipo_documento(str , Enum):
    Curso='Curso'
    Generico='Generico'

class tipo_categoria(str, Enum):
    Programa='Programa'
    Contenido="Contenido"
    Malla='Malla'
    Requisitos='Requisitos'
    Informacion_General='Informacion_General'
    FAQ='FAQ'
# ---------------------------------

class Documento(BaseModel):
    session_id: int = Field(gt=0)
    curso_id: int = Field(gt=0)
    documento: object
    tipo_de_curso: tipo_documento
    categoria: tipo_categoria
    
    