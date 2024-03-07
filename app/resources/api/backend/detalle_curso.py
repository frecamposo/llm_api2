
detalle_curso=[
    {
        "curso_id":1,
        "detalle":[
            {
                "plan_estudios":"plan numero 1",
                "requisitos":"tener un pc",
                "duracion": "5 semestres"
            }
        ]
    },
        {
        "curso_id":2,
        "detalle":[
            {
                "plan_estudios":"plan numero 2",
                "requisitos":"tener un pc y conexion internet",
                "duracion": "15 semestres"
            }
        ]
    }
]

def buscar_detalle_curso(id_curso:int):
    for item in detalle_curso:
        if item["curso_id"]==id_curso:
            return item
    return False