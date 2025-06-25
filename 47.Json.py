import json 
from urllib import request
url = "https://my.api.mockaroo.com/personas.json?key=95378360"
respuesta = request.urlopen(url)
#print(respuesta)
contenido = respuesta.read()
#print(contenido)
json_obtenido = json.loads(contenido.decode("utf-8"))
#print(json_obtenido)
for persona in json_obtenido:
    print("**************************************************************")
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellidos ']}")
    print(f"Email: {persona['email']}")
    print("**************************************************************")
    print("\n")
