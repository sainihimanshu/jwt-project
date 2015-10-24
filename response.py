import flask
import json

class Response:

    def json(self, obj, status=200):
        return flask.Response(
            response=json.dumps(obj),
            status=status,
            mimetype='application/json'
        )

    def msg(self, msg, status=200):
        return self.json({'msg': msg}, status)

    def not_found(self):
        return self.msg('Not Found', 404)

    def not_allowed(self):
        return self.msg('Not Allowed', 401)

