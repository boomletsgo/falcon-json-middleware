from falcon import testing

from . import MiddlewareTestsMixin


class RequestEndpoint(object):

    def on_post(self, req, resp, **kwargs):
        resp.json = req.json


class TestRequest(MiddlewareTestsMixin, testing.TestBase):

    def setUp(self):
        super(TestRequest, self).setUp()
        self.api.add_route("/", RequestEndpoint())

    def test_returns_early_if_no_legitimate_data_sent(self):
        client = testing.TestClient(self.api)
        result = client.simulate_post("/", body="  ")

        assert result.status_code == 200
        assert result.text == ""

    def test_json_properly_mirrored(self):
        client = testing.TestClient(self.api)
        result = client.simulate_post("/", body="{\"test\": \"content\"}")

        assert result.status_code == 200
        assert result.text == "{\"test\": \"content\"}"

    def test_json_fails_with_value_error_if_not_valid(self):
        client = testing.TestClient(self.api)
        result = client.simulate_post("/", body="{\"invalid\": 'content'}")

        assert result.status_code == 400

    def test_json_fails_if_invalid_unicode(self):
        client = testing.TestClient(self.api)
        result = client.simulate_post("/", body="garbage".encode("utf-16"))

        assert result.status_code == 400
