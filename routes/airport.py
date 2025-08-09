from flask import Blueprint, request
from services import airport,airport_airline
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
        return return_airport,200
    return {"message":"Exception occured, Please retry"},200
    
@airport_blueprint.route('/get_airport')
def get_airport():
    data = request.args.get("code",default='',type=str)
    try:
        return_airport = airport.get_airport_by_code_handler(data['code'])
        if return_airport:
            return return_airport,200
        return {"message":"Airport Not found"},200
    except Exception as e:
        return {"message":"Exception occured, Please retry"},200

@airport_blueprint.route("/update_airport",methods = ['POST'])
def update_airport():
    data = request.json
    return_airport = airport.update_airport(data)
    if return_airport:
        return {"message":"Update successfull","data":return_airport},200
    return {"message":"Update failed, Please retry"},200

@airport_blueprint.route("/update_airline_status",methods= ['POST'])
def update_airline_status():
    data = request.json
    try:
        return_mapping = airport_airline.update_airport_airline_mapping(data=data)
        if return_mapping:
            return return_mapping,200
        return {"message":"Airport Not found"},200
    except Exception as e:
        return {"message":"Exception occured, Please retry"},200



