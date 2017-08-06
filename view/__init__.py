''' base view '''
import tornado.web
import json

from config import OPRIGIN_ADDRESS, COOKIE_USER

class Route(object):
    urls = []

    def __call__(self, url, name=None):
        def _(cls):
            self.urls.append(tornado.web.URLSpec(url, cls, name=name))
            return cls
        return _

router = Route()

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', OPRIGIN_ADDRESS)
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header(
            'Access-Control-Allow-Headers',
            'Origin, X-Requested-With, Content-Type, Accept')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Content-type', 'application/json')
        self.set_header('Accept', 'application/json')

class SecureHandler(BaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie(COOKIE_USER)

@router('/')
class IndexHandler(BaseHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        return self.write(greeting + ', friendly user!')

    def post(self):
        greeting = json.loads(self.request.body.decode('utf-8'))
        guest = ''
        if i:
            for i in greeting:
                guest += (greeting[i] + ', ')
            return self.finish(guest + 'friendly user!')
        else:
            return self.write('Hello, friendly user!')

def get_post_json(request):
    try:
        return json.loads(request.body.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        return None
