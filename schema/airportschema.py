from marshmallow import Schema,fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

    
# class AirportSchema(Schema):
#     id = fields.UUID(dump_only=True)
#     name = fields.String(required=True)
#     code = fields.String(required=True)
#     location = fields.String(required=True)
#     terminals = fields.Nested('TerminalSchema', many=True, dump_only=True)
#     runways = fields.Nested('RunwaySchema', many=True, dump_only=True)

# schemas/airport_schema.py
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import Airport,Terminal,Runway
from marshmallow_sqlalchemy.fields import Nested



class AirportSchema(SQLAlchemySchema):
    class Meta:
        model = Airport
        load_instance = True

    id = auto_field()
    name = auto_field()
    code = auto_field()
    location = auto_field()


class AirportFullSchema(SQLAlchemySchema):
    class Meta:
        model = Airport
        load_instance = True

    id = auto_field()
    name = auto_field()
    code = auto_field()
    location = auto_field()
    terminals = Nested("TerminalSchema", many=True, dump_only=True)
    runways = Nested("RunwaySchema", many=True, dump_only=True)

class TerminalSchema(SQLAlchemySchema):
    class Meta:
        model = Terminal
        load_instance = True

    id = auto_field()
    number = auto_field()
    capacity = auto_field()
    status = auto_field()


