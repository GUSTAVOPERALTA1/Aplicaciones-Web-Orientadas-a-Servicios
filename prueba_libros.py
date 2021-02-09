import requests
import json

result = requests.get("https://www.etnassoft.com/api/v1/get/?id=589&callback=?")

libro = result.json()
item= libro
encoded= json.dumps(item)
decoded= json.loads(encoded)

titulo_libro=str(decoded[0]["title"][0])
print(titulo_libro)

autor=str(decoded[0]["author"][0])
print(autor)

imagen=str(decoded[0]["thumbnail"][0])
print(imagen)

sinopsis= str(decoded[0]["content_short"][0])
print(sinopsis)

paginas= str(decoded[0]["pages"][0])
print(paginas)

idioma= str(decoded[0]["language"][0])
print(idioma)

descarga= str(decoded[0]["url_download"][0])
print(descarga)

print(libro)
