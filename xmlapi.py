from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from json2xml import json2xml as j2x
from json2xml.utils import readfromurl, readfromstring, readfromjson

app = Flask(__name__)
api = Api(app)


class json2xmlAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('json', type=str, required=False)
        super(json2xmlAPI, self).__init__()

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response('<!doctype html><title>JSON2XML API</title><h1>JSON2XML API</h1>', 200, headers)

    def post(self):
        data = self.reqparse.parse_args()

        if data['json']:
            try:
                # readjson = ""
                # readjson = data['json']
                # print(data['json'])
                readjson = readfromstring(data['json'])
                returning = j2x.Json2xml(readjson, wrapper="all", pretty=True).to_xml()
                print(returning)
                headers = {'Content-Type': 'text/xml'}
                return make_response(returning, 200, headers)
            except:
                return {
                    'json': 'Not json given!'
                }

        else:
            return {
                'json': 'Something when wrong!'
            }


class HelloWorld(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response('<!doctype html><title>JSON2XML API - Framework</title><h1>JSON2XML Framework</h1>', 200, headers)


api.add_resource(HelloWorld, '/')
api.add_resource(json2xmlAPI, '/api')

if __name__ == '__main__':
    print(str("* Starting Flask server..."
              "Please wait until server has fully started."))
    app.run(host="0.0.0.0", debug=True, threaded=False, port="1234")
