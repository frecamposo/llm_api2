from ..models.documento import Documento
from ..backend.conversores.dpf_text.convertir import *
from ..backend.conversores.word_text.convertir import *
from pathlib import Path
import random as rnd


documentos =[
    {
        "session_id": 10,
        "curso_id": 10,
        "id_documento":100
    },
    {
        "session_id": 11,
        "curso_id": 12,
        "id_documento":200
    }

]


def carga_documento(documento: Documento):
    extension= Path(documento.documento).suffix
    print(extension)  
    path=documento.documento
    sw=False
    match extension.upper():
        case '.PDF':
            sw=True
            texto=convertir_pdf(path)
            print(texto)  # --> Texto convertido 
        case '.DOCX':
            sw=True
            texto=convertir_word(path)
            print(texto) # --> Texto convertido 
        case '.TXT':
            sw=True
            fichero=open(documento.documento)
            print(fichero.read())
            
    if sw:
        return texto #rnd.randint(0,1000000)
    else:
        return "No Cargo Archivo, posee diferente extension"



def eliminar_documento(session_id: int, curso_id:int,id_documento:int):
    for item in documentos:
        if item["session_id"]==session_id and  item["curso_id"]==curso_id and  item["id_documento"]==id_documento:
            documentos.remove(item)
            return True
    return False 