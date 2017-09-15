import json

import falcon


class Middleware(object):

    def process_request(self, req, resp):
        req.json = {}

        if not req.content_length:
            return

        body = req.stream.read().strip()

        if not body:
            return

        try:
            req.json = json.loads(body.decode('utf-8'))
        except:
            raise falcon.HTTPBadRequest()

    def process_response(self, req, resp, resource, req_succeeded):
        data = getattr(resp, "json", None)
        if data:
            resp.body = json.dumps(data)
