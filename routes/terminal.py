from flask import Blueprint, request
from services import terminal
from schema.schemas import TerminalCreateSchema,TerminalSchema
terminal_blueprint = Blueprint('terminal', __name__,
                        template_folder='templates')
terminal_schema = TerminalCreateSchema()
terminal_schema_full = TerminalSchema()
@terminal_blueprint.route('/create_terminal',methods = ['POST'])
def create_terminal():
    data = request.json
    return_terminal = terminal.create_terminal(data=data)
    if return_terminal:
        return return_terminal,200
    return {"message":"Exception occured, Please retry"},200
    
@terminal_blueprint.route('/get_terminal')
def get_terminal():
    airport_id = request.args.get("airport_id",default="",type=str)
    number = request.args.get("number",default="",type=str)
    try:
        return_terminal = terminal.get_terminal_by_airport_and_number_handler(code=airport_id,number=number)
        if return_terminal:
            return return_terminal,200
        return {"message":"Airport Not found"},200
    except Exception as e:
        return {"message":"Exception occured, Please retry"},200


@terminal_blueprint.route("/update_terminal",methods = ['POST'])
def update_terminal():
    data = request.json
    return_terminal = terminal.update_terminal(data)
    if return_terminal:
        return {"message":"Update successfull","data":terminal_schema_full.dump(return_terminal)},200
    return {"message":"Update failed, Please retry"},200



