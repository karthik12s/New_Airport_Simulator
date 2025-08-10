from sqlalchemy import update
from models import Gate
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import GateCreateSchema,GateSchema
from services.terminal import get_terminal_by_airport_and_number_handler
gate_schema = GateCreateSchema()
gate_schema_full = GateSchema()
def create_gate(data):
    """
    Creates a new gate using validated input data.
    """
    try:
        # Create the Gate object
        gate_inputs = gate_schema.load(data= data,session=db_session)
        print(gate_inputs)
        terminal = get_terminal_by_airport_and_number_handler(code=gate_inputs['airport_code'],number=gate_inputs['terminal_number'])
        gate_search_result = get_gate_by_terminal_and_number(airport_code=terminal['airport_id'],terminal_number=terminal['number'],number=gate_inputs['number'])
        print(gate_search_result)
        if gate_search_result == None:
            gate_inputs['terminal_id'] = terminal['id']
            del gate_inputs['airport_code']
            del gate_inputs['terminal_number']
            gate_inputs_sch = gate_schema_full.load(gate_inputs,session=db_session)
            db_session.add(gate_inputs_sch)
            db_session.commit()
            return gate_schema_full.dump(gate_inputs)

        return gate_schema_full.dump(gate_search_result) 

    except SQLAlchemyError as e:
        print(e,"line 26")
        db_session.rollback()
    return None

def update_gate(data):
    try:
        gate = get_gate_by_terminal_and_number(airport_code=data['airport_code'],terminal_number=data['terminal_number'],number=data['number'])
        if not gate:
            return None
        for key, value in data.items():
            setattr(gate, key, value)
        db_session.commit()
        print(gate)
        return gate_schema_full.dump(gate) 
    except Exception as e:
        print(e)
    return None
def get_gate_by_terminal_and_number(airport_code = '',terminal_number = '',number = '0'):
    terminal = get_terminal_by_airport_and_number_handler(code=airport_code,number=terminal_number)
    print(terminal,airport_code,terminal_number,number)
    if terminal:
        return db_session.query(Gate).filter_by(terminal_id = terminal['id'],number = number).first()
    return None

def get_gate_by_terminal_and_number_handler(airport_code = '',terminal_number = '',number = '0'):
    return gate_schema_full.dump(get_gate_by_terminal_and_number(airport_code=airport_code,terminal_number=terminal_number,number=number))

gate_schema_full_multi = GateSchema(many=True)

def get_gates_by_terminal(airport_code = '',terminal_number = ''):
    terminal = get_terminal_by_airport_and_number_handler(code=airport_code,number=terminal_number)
    print(terminal,airport_code,terminal_number)
    if terminal:
        return db_session.query(Gate).filter_by(terminal_id = terminal['id']).all()
    return None

def get_gates_by_terminal_handler(airport_code = '',terminal_number = ''):
    return gate_schema_full_multi.dump(get_gates_by_terminal(airport_code=airport_code,terminal_number=terminal_number))

