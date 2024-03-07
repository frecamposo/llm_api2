from models.curso import Curso
import random as rnd

cursos =[
    {
        "session_id": 10,
        "nombre_curso": 'informatica',
        "tipo_de_curso": 'Curso'
    },
    {
        "session_id": 20,
        "nombre_curso": 'informatica 2',
        "tipo_de_curso": 'Video'
    }

]

def agregar_nuevo_curso(curso: Curso):
    cursos.append(curso)
    return rnd.randint(0,1000000)    

def listado_de_cursos():
    return cursos