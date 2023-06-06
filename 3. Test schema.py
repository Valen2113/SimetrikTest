import requests
import jsonschema

url = "https://jsonplaceholder.typicode.com/todos/1"

# Enviar solicitud
response = requests.get(url)

# Validar la respuesta exitosa
if response.ok:
    print("Respuesta exitosa: OK")
else:
    print(f"Respuesta exitosa: {response.status_code}")

# Validar la respuesta del esquema
schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["userId", "id", "title", "completed"]
}

try:
    jsonschema.validate(response.json(), schema)
    print("Respuesta del esquema: Válida")
except jsonschema.exceptions.ValidationError as e:
    print(f"Respuesta del esquema: Inválida - {e}")
