import web

urls = ('/', 
  'api_libra_api.index.Index'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()