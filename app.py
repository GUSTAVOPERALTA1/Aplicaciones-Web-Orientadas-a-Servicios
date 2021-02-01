import web

urls= (
    "/","google_books.index.Index"
)

app= web.application(urls, globals()) #Metodo de libreria web
if __name__=="__main__":
  app.run()