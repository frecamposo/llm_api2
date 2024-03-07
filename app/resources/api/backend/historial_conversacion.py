
respuestas =[
    {
        "pregunta": "de que trata el curso",
        "resuesta": "el curso esta orientado al desarrollo personal",
        "Categoria": "Descripcion Curso",
        "Confiabilidad":"Confianza",
        "Explicabilidad":"NN",
        "Sugerencia":"si quieres saber mas del curso visita nuestra web http://capacitate.com/curso_2323"
    },
    {
        "pregunta": "debo tener conocimientos previos para el curso",
        "resuesta": "no es necesario ya que la metodologia de aprendizaje es esta orientada de forma personal para el estudiante",
        "Categoria": "Requisitos",
        "Confiabilidad":"Pertinencia",
        "Explicabilidad":"NN",
        "Sugerencia":"en el sgte link encontraras informacion sobre los requisitos para el curso http://capacitate.com/requisitos"
    }

]

conversaciones=[
    {
        "session_id":1,
        "historial":respuestas
    }    
]

def recuperar_historial(session_id:id):
    for item in conversaciones:
        if item["session_id"]==session_id:
            return item["historial"]    
    return False