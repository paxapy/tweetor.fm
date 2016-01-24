import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


def make_app():
    return tornado.web.Application([
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'}),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
"""
curl
--get 'https://api.twitter.com/1.1/statuses/user_timeline.json'
--data 'count=3&screen_name=paxapy'
--header 'Authorization: OAuth oauth_consumer_key="",
oauth_nonce="", oauth_signature="",
oauth_signature_method="HMAC-SHA1",
oauth_timestamp="1453661320",
oauth_token="",
oauth_version="1.0"' --verbose
"""