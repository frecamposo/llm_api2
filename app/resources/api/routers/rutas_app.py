from fastapi import APIRouter, Query
from backend.general import *
from models.general import *

rutas = APIRouter()


@rutas.post('/login')
async def validar_login(usuario: Usuario):
    return validacion_cuenta(usuario)

@rutas.post('/cargar_documento')
async def cargar_documento(documento: Documento):
    return carga_documento(documento)

@rutas.post('/eliminar_documento')
async def eliminar_doc(session_id: int,curso_id:int,id_documento:int):
    return eliminar_documento(session_id,curso_id,id_documento)

@rutas.post('/agergar_curso')
async def agregar_curso(curso: Curso):
    return agregar_nuevo_curso(curso)

@rutas.post('/realizar_pregunta')
async def realiza_pregunta(pregunta: Pregunta):
    return respuesta_a_pregunta(pregunta)

@rutas.get('/retornar_cabecera')
async def cabecera(session_id:int = Query(gt=0)):
    return retornar_cabecera(session_id)

@rutas.post('/modificar_cabecera')
async def modifica_la_cabecera(usuario:Usuario):
    return modificar_cabecera(usuario)

@rutas.get('/historial_conversaciones')
async def historial(session_id: int):
    return recuperar_historial(session_id)

@rutas.post('/grabar_contexto')
async def grabar_contexto(session_id:int,contexto:str):
    return grabar_el_contexto(session_id,contexto)

@rutas.get('/listar_contexto')
async def listar_contexto(session_id:int):
    return buscar_contexto(session_id)

@rutas.get('/resumen_conversacion')
async def resumen_conversacion(session_id:int):
    return buscar_resumen_id(session_id)

@rutas.post('/cerrar_sesion')
async def cerrar_sesion(session_id:int):
    pass

@rutas.get('/listado de cursos')
async def listado_de_los_cursos():
    return listado_de_cursos()

@rutas.get('/detalle_curso')
async def detalle_del_curso(id_curso:int):
    return buscar_detalle_curso(id_curso)


@rutas.post('/crear_ticket')
async def generar_ticket(problema:str):
    return crear_ticket(problema)