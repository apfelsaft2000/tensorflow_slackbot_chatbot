import json
import falcon

import func_wakati as fc


class AppResource(object):

    def on_post(self, req, resp):
        body = req.stream.read()
        data = json.loads(body)

        waka1 = fc.wakati(data['in1'])
        waka2 = fc.wakati(data['in2'])


        msg = {'out1' : waka1,
               'out2' : waka2}
        resp.body = json.dumps(msg)


app = falcon.API()
app.add_route("/", AppResource())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
