from pydantic import BaseModel, Field
from typing import Optional

class Usuario(BaseModel):
    username: str
    password:str = Field(default="NN", min_length=2,max_length=20,title="Password")
    inicio_anonimo: bool = Field(default=True,title="Inicio Anonimo o como Administrador")
    session_id: Optional[int]
    nombre:Optional[str]
    ubicacion:Optional[str]