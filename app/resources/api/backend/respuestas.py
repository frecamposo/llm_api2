from ..models.pregunta import Pregunta


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

def respuesta_a_pregunta(pregunta: Pregunta):
    for item in respuestas:
        if item["pregunta"]==pregunta.pregunta:
            return item
    return False 