# encoding:utf-8
"""
首页handler
"""
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index1.html',
                    title="首页")
