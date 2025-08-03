from flask import Blueprint, request
from services import airport
from schema.airportschema import AirportSchema
from database import db_session
airport_blueprint = Blueprint('airport', __name__,
                        template_folder='templates')
@airport_blueprint.route('/create_airport',methods = ['POST'])
def create_airport():
    print(request.json)
    airport_inputs = AirportSchema().load(data= request.json)
    print(airport_inputs)
    db_session.add(airport_inputs)
    db_session.commit()
    
    return AirportSchema.dump(airport_inputs), 201
    

def add_terminal():
    pass

def add_runway():
    pass

def get_runways():
    pass

def get_terminal():
    pass

def add_airline():
    pass



