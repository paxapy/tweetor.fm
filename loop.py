import json
import oauth2
import tornado.ioloop
import tornado.web

import keys


def get_tweets(username):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}'.format(username)
    consumer = oauth2.Consumer(key=keys.KEY, secret=keys.SECRET)
    token = oauth2.Token(key=keys.TOKEN, secret=keys.TOKEN_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method='GET')
    return [tw.get('text') for tw in json.loads(content)]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('page.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        tweets = get_tweets(username)
        self.render('page.html', tweets=tweets)


def make_app():
    return tornado.web.Application([
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'}),
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
