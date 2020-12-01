from marshmallow import Schema, fields, post_load

class Payload(Schema):
    datetime_flag = fields.Boolean(required=True)


class Result(Schema):
    now = fields.DateTime(required=True)



