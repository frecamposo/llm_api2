import random

tickets=[
    
]

def crear_ticket(problema:str):
    num_atencion= random.randint(0,10000)
    texto={"problema":problema,'id_ticket':num_atencion}
    tickets.append(texto)
    return {"confirmacion":True,"numero_ticket":num_atencion}