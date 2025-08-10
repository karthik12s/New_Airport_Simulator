from flask import Blueprint, request
from services import flight
from schema.schemas import FlightCreateSchema,FlightOutputSchema
flight_blueprint = Blueprint('flight', __name__,
                        template_folder='templates')
flight_schema = FlightCreateSchema()
flight_schema_full = FlightOutputSchema()
@flight_blueprint.route('/create_flight',methods = ['POST'])
def create_flight():
    data = request.json
    return_flight = flight.create_flight(data=data)
    if return_flight:
        return return_flight,200
    return {"message":"Exception occured, Please retry"},200
    
@flight_blueprint.route('/get_flight')
def get_flight():
    flight_code = request.args.get("flight_code",default='',type=str)
    try:
        return_flight = flight.get_flight_by_code_handler(flight_code=flight_code)
        if return_flight:
            return return_flight,200
        return {"message":"Flight Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@flight_blueprint.route('/get_flights_for_airline')
def get_flight_for_terminal():
    airline_code = request.args.get("airline_code",default='',type=str)
    try:
        return_flight = flight.get_flights_by_params(airline=airline_code)
        if return_flight:
            return return_flight,200
        return {"message":"Flight Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200



@flight_blueprint.route("/update_flight",methods = ['POST'])
def update_flight():
    data = request.json
    return_flight = flight.update_flight(data)
    if return_flight:
        return {"message":"Update successfull","data":return_flight},200
    return {"message":"Update failed, Please retry"},200








# def create_flight():
#     pass

# def update_flight_status():
#     pass

# def assign_flight():
#     pass

# def update_terminal():
#     pass

# def update_details():
#     pass

# def get_details():
#     pass

# def get_capacity():
#     pass

# def update_capacity():
#     pass