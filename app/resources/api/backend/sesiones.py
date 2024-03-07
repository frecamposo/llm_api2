sessiones=[
    {
        "session_id":1
    },
    {
        "session_id":2
    },
    {
        "session_id":3
    }
]

def cerrar_sesion(session_id:int):
    for item in sessiones:
        if item["session_id"]==session_id:
            sessiones.remove(item)
            return True
    return False


