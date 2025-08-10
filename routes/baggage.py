from flask import Blueprint, request
from services import baggage
from schema.schemas import BaggageBeltCreateSchema,BaggageBeltOutputSchema
from database import db_session
baggage_blueprint = Blueprint('baggage', __name__,
                        template_folder='templates')
baggage_schema = BaggageBeltCreateSchema()
baggage_schema_full = BaggageBeltOutputSchema()
@baggage_blueprint.route('/create_baggage',methods = ['POST'])
def create_baggage():
    data = request.json
    return_baggage = baggage.create_baggage(data=data)
    if return_baggage:
        return return_baggage,200
    return {"message":"Exception occured, Please retry"},200
    
@baggage_blueprint.route('/get_baggage')
def get_baggage():
    airport_code = request.args.get("airport_code",default='',type=str)
    terminal_number = request.args.get("terminal_number",default='',type=str)
    number = request.args.get("number",default='',type=str)
    try:
        return_baggage = baggage.get_baggage_by_terminal_and_number_handler(airport_code=airport_code,terminal_number=terminal_number,number=number)
        if return_baggage:
            return return_baggage,200
        return {"message":"Baggage Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@baggage_blueprint.route('/get_baggages_for_terminal')
def get_baggage_for_terminal():
    airport_code = request.args.get("airport_code",default='',type=str)
    terminal_number = request.args.get("terminal_number",default='',type=str)
    try:
        return_baggage = baggage.get_baggages_by_terminal_handler(airport_code=airport_code,terminal_number=terminal_number)
        if return_baggage:
            return return_baggage,200
        return {"message":"Baggage Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@baggage_blueprint.route('/get_baggage_capacity')
def get_baggage_capacity():
    airport_code = request.args.get("airport_code",default='',type=str)
    terminal_number = request.args.get("terminal_number",default='',type=str)
    number = request.args.get("number",default='',type=str)
    try:
        return_baggage = baggage.get_baggage_by_terminal_and_number_handler(airport_code=airport_code,terminal_number=terminal_number,number=number)
        if return_baggage:
            return {"message":"Baggage found",'data':return_baggage['capacity']},200
        return {"message":"Baggage Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@baggage_blueprint.route("/update_baggage",methods = ['POST'])
def update_baggage():
    data = request.json
    return_baggage = baggage.update_baggage(data)
    if return_baggage:
        return {"message":"Update successfull","data":return_baggage},200
    return {"message":"Update failed, Please retry"},200


@baggage_blueprint.route("/update_baggage_status_for_terminal",methods = ['POST'])
def update_baggage_status_by_terminal():
    data = request.json
    return_baggage = baggage.bulk_update_baggage_status(data['airport_code'],data['terminal_number'],data['status'])
    if return_baggage:
        return {"message":"Update successfull","data":return_baggage},200
    return {"message":"Update failed, Please retry"},200





def create_baggage():
    pass

def update_baggage_status():
    pass

def assign_flight():
    pass

def update_terminal():
    pass

def update_details():
    pass

def get_details():
    pass

def get_capacity():
    pass

def update_capacity():
    pass