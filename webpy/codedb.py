# -*- coding: utf-8 -*-
import web

render = web.template.render('../template')
urls = (
    '/', 'index2',
    '/add', 'add'
)
db = web.database(dbn='mysql', user='qqbwww', pw='wwwqqb', db='test')


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
