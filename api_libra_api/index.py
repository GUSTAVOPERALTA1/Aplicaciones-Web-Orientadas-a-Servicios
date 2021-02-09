import web
import requests
import json

render= web.template.render("api_libra_api/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self)  :
    form=web.input()
    bookname=form.bookname
    
    result = requests.get("https://www.etnassoft.com/api/v1/get/?id=589&callback=?"+bookname)

    libro = result.json()
    item= libro
    encoded= json.dumps(item)
    decoded= json.loads(encoded)

    titulo_libros=str(decoded[0]["title"][0])
    autores=str(decoded[0]["author"][0])
    imagenes=str(decoded[0]["thumbnail"][0])
    resumen= str(decoded[0]["content_short"][0])
    pag= str(decoded[0]["pages"][0])
    idiomas= str(decoded[0]["language"][0])
    descargas= str(decoded[0]["url_download"][0])

    

    titulo_libros="<label>'"+titulo_libros+"'</label>"
    autores="<label>'"+autores+"'</label>"
    imagenes= "<label>'"+imagenes+"'</label>"
    resumen= "<label>'"+resumen+"'</label>"
    pag= "<label>'"+pag+"'</label>"
    idiomas= "<label>'"+idiomas+"'</label>"
    descargas= "<label>'"+descargas+"'</label>"


    datos={
      
      "bookname":"El nombre del libro es: "+bookname,
      "titulo":+titulo_libros,
      "autorlibro":"Autor: "+autores,
      "image":"Imagen: "+imagenes,
      "resumen":"Resumen: "+resumen,
      "pag":"Numero de paginas: "+pag,
      "idioma":"Idioma del libro: "+idiomas,
      "adquirir":"Descarga: "+descargas

    }
    return render.index(datos)