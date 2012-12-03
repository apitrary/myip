# -*- coding: utf-8 -*-
"""

    myip

    created by hgschmidt on 03.12.12, 21:53 CET
    
    Copyright (c) 2012 apitrary

"""
import logging
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

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
HTTP_PORT = 8888

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
        if 'X-Real-Ip' in self.request.headers:
            self.write(self.request.headers['X-Real-Ip'])
        else:
            self.write(self.request.headers)


# FUNCTIONS
#
#
def start_tornado_server(port=HTTP_PORT):
    """
        Start the Tornado server
    """
    # Setup the application context
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

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

