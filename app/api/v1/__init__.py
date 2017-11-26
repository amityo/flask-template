"""
Creates Blueprint and imports endpoints
"""

from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(app=blueprint, version=1.0, title="Api v1")

# import endpoints after api is created
from .endpoints import \
    example_namespace

api.add_namespace(example_namespace)
