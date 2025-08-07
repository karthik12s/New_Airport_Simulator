from flask import Blueprint, request
from services import airport
from schema.schemas import AirportCreateSchema,AirportOutputSchema
from database import db_session
airport_blueprint = Blueprint('airport', __name__,
                        template_folder='templates')
airport_schema = AirportCreateSchema()
airport_schema_full = AirportOutputSchema()
@airport_blueprint.route('/create_airport',methods = ['POST'])
def create_airport():
    data = request.json
    return_airport = airport.create_airport(data=data)
    if return_airport:
        return return_airport,201
    return {"message":"Exception occured, Please retry"},201
    
@airport_blueprint.route('/get_airport',methods = ['POST'])
def get_airport():
    data = request.json
    try:
        return_aiport = airport.get_airport_by_code_handler(data['code'])
        if return_aiport:
            return return_aiport,201
        return {"message":"Airport Not found"},201
    except Exception as e:
        return {"message":"Exception occured, Please retry"},201
def add_airline():
    pass



