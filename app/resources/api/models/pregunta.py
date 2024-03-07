from pydantic import BaseModel, Field
# ---------------------------------

class Pregunta(BaseModel):
    session_id: int = Field(gt=0)    
    pregunta: str
    
    