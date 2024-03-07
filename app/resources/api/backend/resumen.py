

resumenes=[
    {
        "session_id":1,
        "resumen":"el futuro alumno realizo una serie de busquedas asociadas a cursos de gastronomia"
    },
        {
        "session_id":2,
        "resumen":"la conversacion esta asociada al ambito de la tecnologia"
    },
            {
        "session_id":3,
        "resumen":"solo observo videos"
    }
]

def buscar_resumen_id(session_id:int):
    for item in resumenes:
        if item["session_id"]==session_id:
            return item
    return False