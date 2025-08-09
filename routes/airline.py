from flask import Blueprint, request
from services import airline,airport_airline
from schema.schemas import AirlineCreateSchema,AirlineOutputSchema
airline_blueprint = Blueprint('airline', __name__,
                        template_folder='templates')
airline_schema = AirlineCreateSchema()
airline_schema_full = AirlineOutputSchema()
@airline_blueprint.route('/create_airline',methods = ['POST'])
def create_airline():
    data = request.json
    return_airline = airline.create_airline(data=data)
    if return_airline:
        return return_airline,201
    return {"message":"Exception occured, Please retry"},201
    
@airline_blueprint.route('/get_airline')
def get_airline():
    code = request.args.get("code",default="",type=str)
    try:
        return_airport = airline.get_airline_by_code_handler(code)
        if return_airport:
            return return_airport,201
        return {"message":"Airline Not found"},201
    except Exception as e:
        return {"message":"Exception occured, Please retry"},201

@airline_blueprint.route("/update_airline",methods = ['POST'])
def update_airline():
    data = request.json
    return_airline = airline.update_airline(data)
    if return_airline:
        return {"message":"Update successfull","data":return_airline},201
    return {"message":"Update failed, Please retry"},201

@airline_blueprint.route("/airline/create_airport_airline_mapping",methods= ['POST'])
def update_airline_status():
    data = request.json
    data['is_approved'] = False
    try:
        return_mapping = airport_airline.create_airport_airline_mapping(data=data)
        print(return_mapping)
        if return_mapping:
            return return_mapping,201
        return {"message":"Airline Not found"},201
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},201



