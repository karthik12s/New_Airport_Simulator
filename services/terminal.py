from models import Terminal
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import TerminalCreateSchema,TerminalSchema
from services.utils import bulk_update_baggage_status,bulk_update_gate_status
terminal_schema = TerminalCreateSchema()
terminal_schema_full = TerminalSchema()
def create_terminal(data):
    """
    Creates a new terminal using validated input data.
    """
    try:
        # Create the Terminal object
        print(data)
        terminal_inputs = terminal_schema.load(data= data,session=db_session)
        print(terminal_inputs)
        terminal_search_result = get_terminal_by_airport_and_number(terminal_inputs.airport_id,terminal_inputs.number)
        if terminal_search_result == None:
            print(terminal_inputs)
            db_session.add(terminal_inputs)
            db_session.commit()
            return terminal_schema_full.dump(terminal_inputs)

        return terminal_schema_full.dump(terminal_search_result) 

    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None

def update_terminal(data):
    terminal = get_terminal_by_airport_and_number(data['airport_id'],number=data['number'])
    if not terminal:
        return None
    for key, value in data.items():
        if key == 'is_active' and terminal.is_active!=value:
            baggage_result = bulk_update_baggage_status(terminal_id=terminal.id,status=value)
            gate_result = bulk_update_gate_status(terminal_id=terminal.id,status=value)
            if not (baggage_result or gate_result):
                return None
        setattr(terminal, key, value)
    db_session.commit()
    return terminal

def get_terminal_by_airport_and_number(airport_id = '',number = '0'):
    return db_session.query(Terminal).filter_by(airport_id=airport_id,number=number).first()

def get_terminal_by_airport_and_number_handler(code,number):
    return terminal_schema_full.dump(get_terminal_by_airport_and_number(code,number))