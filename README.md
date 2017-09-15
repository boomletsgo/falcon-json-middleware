# Falcon JSON Middleware
JSON Middleware for [Falcon Framework](https://falconframework.org/).

[![Build Status](https://travis-ci.org/boomletsgo/falcon-json-middleware.svg?branch=master)](https://travis-ci.org/boomletsgo/falcon-json-middleware)
[![PyPI](https://img.shields.io/pypi/v/falcon-json-middleware.svg)](https://pypi.python.org/pypi/falcon-json-middleware/)
[![Python Versions](https://img.shields.io/pypi/pyversions/falcon-json-middleware.svg)](https://pypi.python.org/pypi/falcon-json-middleware/)
[![Coverage Status](https://coveralls.io/repos/boomletsgo/falcon-json-middleware/badge.svg?branch=master)](https://coveralls.io/r/boomletsgo/falcon-json-middleware?branch=master)




## Installation

`$ pip install falcon-json-middleware`

## Usage

Inside your application file:

```
import falcon
import falcon_json_middleware

middleware = [falcon_json_middleware.Middleware()]

class IndexEndpoint(object):
	"""Example API endpoint to show basics of usage"""

	def on_get(self, req, resp):
		resp.json = {"status": "OK"}

	def on_post(self, req, resp):
		name = req.json["name"]
		resp.json = {"name": name}

application = falcon.API(middleware=middleware)
application.add_route("/", IndexEndpoint())
```

Now, start up your app with your wsgi server of choice and do a `GET /` and you should see a JSON response. You can also send in a `POST` with a "name" key in the data and it will be returned.
