from flask_restx import Namespace, Resource
from flask_accepts import accepts, responds
from app.apis.dto import Payload, Result
from flask import request
from datetime import datetime

marvik_ns = Namespace("marvik", description="Marvik Test App")

@marvik_ns.route("/")
class GetDate(Resource):
    @accepts(schema=Payload, api=marvik_ns)
    @responds(schema=Result, api=marvik_ns)
    def post(self):
        parsed = request.parsed_obj
        payload = Payload().load(parsed)
        if payload["datetime_flag"]:
            fmt =  "%Y-%m-%d %H:%M:%S"
        else:
            fmt = "%Y-%d-%m" 
        now_str = datetime.now().strftime(fmt)
        result = Result().load({"now": now_str})
        return result

