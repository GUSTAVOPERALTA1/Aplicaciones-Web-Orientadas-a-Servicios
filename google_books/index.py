import web
render= web.template.render("google_books/")
class Index():
  def GET(self): #Metodo para reenderizar y mostrar la pagina
    return render.index()