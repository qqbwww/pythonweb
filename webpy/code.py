'''
import web
from web.db import sqlliteral

render = web.template.render('../template')
urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name):
        i = web.input(name= None)
        return render.index(i.name)

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
    '''