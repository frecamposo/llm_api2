from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# --------------------------------- Creacion de Tipos
class tipo_curso(str , Enum):
    Tutorial='Tutorial'
    Video='Video'
    Curso='Curso'
# ---------------------------------

class Curso(BaseModel):
    session_id: int = Field(gt=0)
    nombre_curso: str = Field(min_length=2,max_length=300)
    tipo_de_curso: tipo_curso
    