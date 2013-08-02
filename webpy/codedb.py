# -*- coding: utf-8 -*-
import web

render = web.template.render('../template')
html5render = web.template.render('../template/html5')
urls = (
    '/', 'index2',
    '/add', 'add',
    '/html5', 'html5',
    '/html5/basic', 'basic',

)
db = web.database(dbn='mysql', user='qqbwww', pw='wwwqqb', db='test')


class html5:
    def GET(self):
        return html5render.html5()


class basic:
    def GET(self):
        return html5render.basic()


class index2:
    def GET(self):
        todos = db.select('todo')
        return render.index2(todos)


class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
