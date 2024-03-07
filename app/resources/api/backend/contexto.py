
contextos=[
    {
        "session_id":1,
        "contexto":"informacion del curso de finanzas"
    },
    {
        "session_id":2,
        "contexto":"periodos de postulacion"
    }
]

def buscar_contexto(session_id:int):
    for item in contextos:
        if item["session_id"]==session_id:
            return item
    return False

def grabar_el_contexto(session_id:int, contexto:str):
    cont={"session_id":session_id,"contexto":contexto}
    contextos.append(cont)
    return True