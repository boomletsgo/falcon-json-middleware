from falcon import testing

from . import MiddlewareTestsMixin


class ResponseEndpoint(object):

    def on_get(self, req, resp, **kwargs):
        resp.json = {"status": "OK"}


class TestResponse(MiddlewareTestsMixin, testing.TestBase):

    def setUp(self):
        super(TestResponse, self).setUp()
        self.api.add_route("/", ResponseEndpoint())

    def test_json_present_in_request(self):
        client = testing.TestClient(self.api)
        result = client.simulate_get("/")

        assert result.status_code == 200
        assert result.text == "{\"status\": \"OK\"}"
