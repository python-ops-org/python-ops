import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    
    def post(self):
        body = self.request.body
        if not body:
            self.set_status(400)
        elif 'AnsibleTower' in self.request.headers and self.request.headers['AnsibleTower'] == 'xSecretx':
            print("Request dictionary: {}".format(body))
            self.write({"status": "triggered"})
            self.set_status(201)
        else:
            self.write({"status": "ok"})
            self.set_status(200)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/push", MainHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
