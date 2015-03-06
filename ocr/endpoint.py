__author__ = 'RiteshReddy'
import sys
sys.path.append("Lib/site-packages")


# noinspection PyUnresolvedReferences
from flask import Flask, request

# noinspection PyUnresolvedReferences
from flask.ext.restful import Resource, Api, reqparse

from ocr import ReceiptOCR


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('image64', type=str, help='Data Missing', required=True)

class OCREndpoint(Resource):
    def get(self):
        pass

    def post(self):
        args = parser.parse_args()
        image_64 = args['image64']
        try:
            ocr = ReceiptOCR(image_64)
            return {"structure" : ocr.get_structure(),
                    "raw": ocr.convert_to_text()}
        except Exception,e:
            return {"error": str(e)}


    def put(self):
        pass

api.add_resource(OCREndpoint, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')