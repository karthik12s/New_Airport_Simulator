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
    
# @flight_blueprint.route('/get_flight')
# def get_flight():
#     airport_code = request.args.get("airport_code",default='',type=str)
#     terminal_number = request.args.get("terminal_number",default='',type=str)
#     number = request.args.get("number",default='',type=str)
#     try:
#         return_flight = flight.get_flight_by_terminal_and_number_handler(airport_code=airport_code,terminal_number=terminal_number,number=number)
#         if return_flight:
#             return return_flight,200
#         return {"message":"Flight Not found"},200
#     except Exception as e:
#         print(e)
#         return {"message":"Exception occured, Please retry"},200

# @flight_blueprint.route('/get_flights_for_terminal')
# def get_flight_for_terminal():
#     airport_code = request.args.get("airport_code",default='',type=str)
#     terminal_number = request.args.get("terminal_number",default='',type=str)
#     try:
#         return_flight = flight.get_flights_by_terminal_handler(airport_code=airport_code,terminal_number=terminal_number)
#         if return_flight:
#             return return_flight,200
#         return {"message":"Flight Not found"},200
#     except Exception as e:
#         print(e)
#         return {"message":"Exception occured, Please retry"},200

# @flight_blueprint.route('/get_flight_capacity')
# def get_flight_capacity():
#     airport_code = request.args.get("airport_code",default='',type=str)
#     terminal_number = request.args.get("terminal_number",default='',type=str)
#     number = request.args.get("number",default='',type=str)
#     try:
#         return_flight = flight.get_flight_by_terminal_and_number_handler(airport_code=airport_code,terminal_number=terminal_number,number=number)
#         if return_flight:
#             return {"message":"Flight found",'data':return_flight['capacity']},200
#         return {"message":"Flight Not found"},200
#     except Exception as e:
#         print(e)
#         return {"message":"Exception occured, Please retry"},200

@flight_blueprint.route("/update_flight",methods = ['POST'])
def update_flight():
    data = request.json
    return_flight = flight.update_flight(data)
    if return_flight:
        return {"message":"Update successfull","data":return_flight},200
    return {"message":"Update failed, Please retry"},200


# @flight_blueprint.route("/update_flight_status_for_terminal",methods = ['POST'])
# def update_flight_status_by_terminal():
#     data = request.json
#     return_flight = flight.bulk_update_flight_status(data['airport_code'],data['terminal_number'],data['status'])
#     if return_flight:
#         return {"message":"Update successfull","data":return_flight},200
#     return {"message":"Update failed, Please retry"},200





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