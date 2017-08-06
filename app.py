''' This is the main entry file for the python version of website '''
# !/usr/bin/python
# Filename: func_doc.py
# _*_coding: utf-8_*_
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define, options, parse_command_line

import config as site_config
from view import router
import view.views

import model.models

define("port", default=site_config.PORT, help="run on the given port", type=int)

setting = {
    'login_url': '/login',
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'cookie_secret': site_config.COOKIE_SECRET,
    "xsrf_cookies": site_config.XSRF_COOKIES,
    'debug': site_config.DEBUG
}

if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(
        handlers=router.urls,
        **setting
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Server runing...\nPlease link: "localhost:%d"' % options.port)
    tornado.ioloop.IOLoop.instance().start()
