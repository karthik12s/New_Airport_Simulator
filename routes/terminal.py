from flask import Blueprint, request
from services import terminal
from schema.schemas import TerminalCreateSchema,TerminalOutputSchema
terminal_blueprint = Blueprint('terminal', __name__,
                        template_folder='templates')
terminal_schema = TerminalCreateSchema()
terminal_schema_full = TerminalOutputSchema()
@terminal_blueprint.route('/create_terminal',methods = ['POST'])
def create_terminal():
    data = request.json
    return_terminal = terminal.create_terminal(data=data)
    if return_terminal:
        return return_terminal,201
    return {"message":"Exception occured, Please retry"},201
    
@terminal_blueprint.route('/get_terminal',methods = ['POST'])
def get_terminal():
    data = request.json
    try:
        return_terminal = terminal.get_terminal_by_airport_and_number_handler(data['airport_id'],data['number'])
        if return_terminal:
            return return_terminal,201
        return {"message":"Airport Not found"},201
    except Exception as e:
        return {"message":"Exception occured, Please retry"},201
def add_airline():
    pass



