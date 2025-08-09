from models import Airline
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import AirlineCreateSchema,AirlineSchema
airline_schema = AirlineCreateSchema()
airline_schema_full = AirlineSchema()
def create_airline(data):
    """
    Creates a new airline using validated input data.
    """
    try:
        # Create the Airline object
        airline_inputs = airline_schema.load(data= data,session=db_session)
        airline_search_result = get_airline_by_code(airline_inputs.code)
        if airline_search_result == None:
            db_session.add(airline_inputs)
            db_session.commit()
            return airline_schema_full.dump(airline_inputs)

        return airline_schema_full.dump(airline_search_result) 

    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None

def update_airline(data):
    try:
        airline = get_airline_by_code(data['code'])
        if not airline:
            return None
        for key, value in data.items():
            setattr(airline, key, value)
        db_session.commit()
        return airline_schema.dump(airline)
    except Exception as e:
        print(e)
    return None
def get_airline_by_code(code):
    return db_session.query(Airline).filter_by(code=code).first()

def get_airline_by_code_handler(code):
    return airline_schema_full.dump(get_airline_by_code(code))
