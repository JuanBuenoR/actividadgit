
from pydantic import BaseModel

class Evento(BaseModel):
    titulo: str
    fecha: str  
    hora: str 
    usuario_id: str
    lugar: str = None 
