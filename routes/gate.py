from flask import Blueprint, request
from services import gate
from schema.schemas import GateCreateSchema,GateOutputSchema
from database import db_session
gate_blueprint = Blueprint('gate', __name__,
                        template_folder='templates')
gate_schema = GateCreateSchema()
gate_schema_full = GateOutputSchema()
@gate_blueprint.route('/create_gate',methods = ['POST'])
def create_gate():
    data = request.json
    return_gate = gate.create_gate(data=data)
    if return_gate:
        return return_gate,200
    return {"message":"Exception occured, Please retry"},200
    
@gate_blueprint.route('/get_gate')
def get_gate():
    airport_code = request.args.get("airport_code",default='',type=str)
    terminal_number = request.args.get("terminal_number",default='',type=str)
    number = request.args.get("number",default='',type=str)
    try:
        return_gate = gate.get_gate_by_terminal_and_number_handler(airport_code=airport_code,terminal_number=terminal_number,number=number)
        if return_gate:
            return return_gate,200
        return {"message":"Gate Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@gate_blueprint.route('/get_gates_for_terminal')
def get_gate_for_terminal():
    airport_code = request.args.get("airport_code",default='',type=str)
    terminal_number = request.args.get("terminal_number",default='',type=str)
    try:
        return_gate = gate.get_gates_by_terminal_handler(airport_code=airport_code,terminal_number=terminal_number)
        if return_gate:
            return return_gate,200
        return {"message":"Gate Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@gate_blueprint.route('/get_gate_capacity')
def get_gate_capacity():
    airport_code = request.args.get("airport_code",default='',type=str)
    terminal_number = request.args.get("terminal_number",default='',type=str)
    number = request.args.get("number",default='',type=str)
    try:
        return_gate = gate.get_gate_by_terminal_and_number_handler(airport_code=airport_code,terminal_number=terminal_number,number=number)
        if return_gate:
            return {"message":"Gate found",'data':return_gate['capacity']},200
        return {"message":"Gate Not found"},200
    except Exception as e:
        print(e)
        return {"message":"Exception occured, Please retry"},200

@gate_blueprint.route("/update_gate",methods = ['POST'])
def update_gate():
    data = request.json
    return_gate = gate.update_gate(data)
    if return_gate:
        return {"message":"Update successfull","data":return_gate},200
    return {"message":"Update failed, Please retry"},200


@gate_blueprint.route("/update_gate_status_for_terminal",methods = ['POST'])
def update_gate_status_by_terminal():
    data = request.json
    return_gate = gate.bulk_update_gate_status(data['airport_code'],data['terminal_number'],data['status'])
    if return_gate:
        return {"message":"Update successfull","data":return_gate},200
    return {"message":"Update failed, Please retry"},200





def create_gate():
    pass

def update_gate_status():
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