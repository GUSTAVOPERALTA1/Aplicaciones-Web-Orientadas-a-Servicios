import web

render = web.template.render("error/")
class Index():
  def GET(self):
    return render.index()