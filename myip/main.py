# /usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""

    myip

    created by hgschmidt on 03.12.12, 21:53 CET
    
    Copyright (c) 2012 otype

"""
import logging

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
from tornado import web


# LOGGING PARAMETERS
#
#
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger('myip')
logger.setLevel(logging.DEBUG)

# PORT
#
#
HTTP_PORT = 65410

# TEMPLATES PATH
#
#
TEMPLATES_DIR = './myip/templates'
STYLES_DIR = './myip/assets'


# CLASSES
#
#
class MainHandler(tornado.web.RequestHandler):
    """
        Very simple handler to display the X-Real-Ip (IP address).
    """

    def __init__(self, application, request, **kwargs):
        """
            Store the request for later reference
        """
        super(MainHandler, self).__init__(application, request, **kwargs)
        self.request = request
        logger.info(self.request)

    def get(self, *args, **kwargs):
        """
            Print out the 'X-Real-Ip' header variable. If not available
            at least spit out the headers.
        """
        if 'X-Real-Ip' in self.request.headers.keys():
            self.render("external.html", my_ip_address=self.request.headers['X-Real-Ip'])
        elif 'X-Forwarded-For' in self.request.headers.keys():
            self.render("external.html", my_ip_address=self.request.headers['X-Forwarded-For'])
        else:
            self.render("local.html", request_headers=self.request.headers)


# FUNCTIONS
#
#
def start_tornado_server(port=HTTP_PORT):
    """
        Start the Tornado server
    """
    # Setup the application context
    handlers = [
        (r"/", MainHandler),
        (r"/static/(.*)", web.StaticFileHandler, {"path": STYLES_DIR}),
    ]

    settings = dict(template_path=TEMPLATES_DIR)
    application = tornado.web.Application(handlers, **settings)

    # Setup the HTTP server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)

    # Ok, we're ready to start!
    tornado.ioloop.IOLoop.instance().start()

# MAIN
#
#
if __name__ == "__main__":
    logger.info('Starting server on port: {http_port}'.format(http_port=HTTP_PORT))
    start_tornado_server()

