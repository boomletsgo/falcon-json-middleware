import falcon
import falcon_json_middleware


class MiddlewareTestsMixin:

    def setUp(self):
        super().setUp()
        self.api = falcon.API(middleware=falcon_json_middleware.Middleware())
