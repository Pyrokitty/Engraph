import web
import rrdtool

urls = ('/','engraph')
render = web.template.render('templates/')

class engraph:
    def GET(self):
        
        return render.engraph('static/e.png')

if __name__ == '__main__':
    app = web.application(urls,globals())
    app.run()
