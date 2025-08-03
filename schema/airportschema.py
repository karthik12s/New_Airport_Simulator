from marshmallow import Schema,fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

    
class AirportSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    code = fields.String(required=True)
    location = fields.String(required=True)
    terminals = fields.Nested('TerminalSchema', many=True, dump_only=True)
    runways = fields.Nested('RunwaySchema', many=True, dump_only=True)
    