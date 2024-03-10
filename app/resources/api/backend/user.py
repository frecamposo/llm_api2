from ..models.usuario import Usuario
import random
import json

lista_usuarios=[
    {
        "session_id":1,
        "username":"juan",
        "password":"lana",
        "inicio_anonimo": True,
        "nombre":"Juan Ortega Miranda",
        "ubicacion":"Oficia Central, Republica #911, Santiago"
    },
    {
        "session_id":2,
        "username":"xx",
        "password":"xx",
        "inicio_anonimo": False ,     
        "nombre":"Marcelo Correa",
        "ubicacion":"Av. Lira #910, Atacama, Chile "
    }
]


def conexion():
    # logica de la conexion y recuperacion de la informacion desde la base de datos
    pass

def validacion_cuenta(usuario: Usuario):
    if usuario.inicio_anonimo:
        valor= random.randint(0,1000000)
        return valor
    for item in lista_usuarios:
        if item['username']== usuario.username and item['password']== usuario.password:
            valor= random.randint(0,1000000)
            return valor
    return "Usuario no encontrado"
    
def retornar_cabecera(session_id:int):
    for item in lista_usuarios:
        if item["session_id"]==session_id:
            texto='{"username":"'+item["username"]+'","nombre": "'+item["nombre"]+'","ubicacion":"'+item["ubicacion"]+'"}'
            return json.loads(texto)
        
def listar_usuarios():
    return lista_usuarios

def modificar_cabecera(usuario:Usuario):
    for index,item in enumerate(lista_usuarios):
        if item['session_id'] == usuario.session_id:
            lista_usuarios[index]['password'] =usuario.password
            lista_usuarios[index]['nombre'] =usuario.nombre
            lista_usuarios[index]['ubicacion'] = usuario.ubicacion
            return True
    return False

