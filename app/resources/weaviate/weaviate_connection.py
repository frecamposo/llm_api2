import weaviate
import json
from embedding_util import generate_embeddings

client = weaviate.Client(
    url="http://34.39.130.2:8080"
)

# Crea una clase de documentos solo con el nombre.
def crear_clase_documento(nombre):
    class_obj = {"class": nombre, "vectorizer": "none"}
    client.schema.create_class(class_obj)

# Carga un documento en formato de string a la clase de documentos escogida.
# A los documentos de la clase solo se les asigna la propiedad de 'texto'
def cargar_documento(texto, nombre_clase):
    with client.batch as batch:
        properties = {"texto": texto}
        vector = generate_embeddings(texto)
        batch.add_data_object(properties, nombre_clase, vector=vector)

# Obtiene todos lso documentos ingresados, retornando la propiedad texto de cada uno.
def obtener_documentos(nombre_clase):
    result = client.query.get(nombre_clase, ["texto"]).do()
    return json.dumps(result, indent=4)

# Funcion para determinar el conjunto de textos en weaviate relacionados con la consulta o pregunta que queremos hacer
def realizar_consulta(consulta, nombre_clase, certeza=0.9, max_documentos=5):
    # Se vectoriza el string de la consulta
    query_vector = generate_embeddings(consulta)

    result = client.query.get(nombre_clase, ["texto"]).with_near_vector({
        "vector": query_vector,
        "certainty": certeza
    }).with_limit(max_documentos).with_additional(['certainty', 'distance']).do()
    
    return json.dumps(result, indent=4)