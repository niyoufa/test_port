# @Time    : 2018/3/26 下午10:11
# @Author  : Niyoufa
import tornado.web
import tornado.gen
from torserver.libs import apilib


class TestHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.p = self.get_argument("p")

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        if self.p == "1":
            response = yield apilib.get("https://google.com")
        elif self.p == "2":
            response = yield apilib.async_get("https://google.com")
        else:
            response = yield apilib.get("https://www.baidu.com")
        self.finish(response.body)


handlers = [
    (r"/api/test", TestHandler),
]