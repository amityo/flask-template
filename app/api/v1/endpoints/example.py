from flask_restplus import Resource
from .. import api

ns = api.namespace('example', description='example')

@ns.route('/')
class Example(Resource):
    def get(self):
        return 'example'
