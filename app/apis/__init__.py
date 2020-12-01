from flask_restx import Api
from app.apis.ping import ping_ns
from app.apis.marvik import marvik_ns
api = Api(title="API",version="1.0", description="descrption")

api.add_namespace(ping_ns)
api.add_namespace(marvik_ns)