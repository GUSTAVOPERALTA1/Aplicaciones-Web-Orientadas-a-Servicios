import web

urls= (
  "/","error.index.Index"
)

app= web.application(urls, globals())

if __name__ == "__main__":
  app.run()