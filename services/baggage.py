from sqlalchemy import update
from models import BaggageBelt
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import BaggageBeltCreateSchema,BaggageBeltSchema
from services.terminal import get_terminal_by_airport_and_number_handler
baggage_schema = BaggageBeltCreateSchema()
baggage_schema_full = BaggageBeltSchema()
def create_baggage(data):
    """
    Creates a new baggage using validated input data.
    """
    try:
        # Create the BaggageBelt object
        baggage_inputs = baggage_schema.load(data= data,session=db_session)
        print(baggage_inputs,list(baggage_inputs))
        terminal = get_terminal_by_airport_and_number_handler(code=baggage_inputs['airport_code'],number=baggage_inputs['terminal_number'])
        baggage_search_result = get_baggage_by_terminal_and_number(airport_code=terminal['airport_id'],terminal_number=terminal['number'],number=baggage_inputs['number'])
        print(baggage_search_result)
        if baggage_search_result == None:
            baggage_inputs['terminal_id'] = terminal['id']
            del baggage_inputs['airport_code']
            del baggage_inputs['terminal_number']
            baggage_inputs_sch = baggage_schema_full.load(baggage_inputs,session=db_session)
            db_session.add(baggage_inputs_sch)
            db_session.commit()
            return baggage_schema_full.dump(baggage_inputs)

        return baggage_schema_full.dump(baggage_search_result) 

    except SQLAlchemyError as e:
        print(e,"line 26")
        db_session.rollback()
    return None

def update_baggage(data):
    try:
        baggage = get_baggage_by_terminal_and_number(airport_code=data['airport_code'],terminal_number=data['terminal_number'],number=data['number'])
        if not baggage:
            return None
        for key, value in data.items():
            setattr(baggage, key, value)
        db_session.commit()
        print(baggage)
        return baggage_schema_full.dump(baggage) 
    except Exception as e:
        print(e)
    return None
def get_baggage_by_terminal_and_number(airport_code = '',terminal_number = '',number = '0'):
    terminal = get_terminal_by_airport_and_number_handler(code=airport_code,number=terminal_number)
    print(terminal,airport_code,terminal_number,number)
    if terminal:
        return db_session.query(BaggageBelt).filter_by(terminal_id = terminal['id'],number = number).first()
    return None

def get_baggage_by_terminal_and_number_handler(airport_code = '',terminal_number = '',number = '0'):
    return baggage_schema_full.dump(get_baggage_by_terminal_and_number(airport_code=airport_code,terminal_number=terminal_number,number=number))

baggage_schema_full_multi = BaggageBeltSchema(many=True)

def get_baggages_by_terminal(airport_code = '',terminal_number = ''):
    terminal = get_terminal_by_airport_and_number_handler(code=airport_code,number=terminal_number)
    print(terminal,airport_code,terminal_number)
    if terminal:
        return db_session.query(BaggageBelt).filter_by(terminal_id = terminal['id']).all()
    return None

def get_baggages_by_terminal_handler(airport_code = '',terminal_number = ''):
    return baggage_schema_full_multi.dump(get_baggages_by_terminal(airport_code=airport_code,terminal_number=terminal_number))

