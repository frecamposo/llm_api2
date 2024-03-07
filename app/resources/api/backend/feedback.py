

feedback_list=[
    {
        "curso_id":1,
        "usuario_id":1,
        "feedback":"me intereso el curso de cocina, es entretenido"
    },
    {
        "curso_id":2,
        "usuario_id":3,
        "feedback":"el curso de computacion es muy util"
    },
    {
        "curso_id":3,
        "usuario_id":4,
        "feedback":"los videos son muy simples de entender"
    }
]

def grabar_feedback(id_curso:int,id_usuario:int,feedback:str):
    text={"curso_id":id_curso,"usuario_id":id_usuario,"feedback":feedback}
    feedback_list.append(text)
    return True