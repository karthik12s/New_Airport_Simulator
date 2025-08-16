from sqlalchemy import update
from models import Flight
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import FlightCreateSchema,FlightSchema
from services.terminal import get_terminal_by_airport_and_number_handler
flight_schema = FlightCreateSchema()
flight_schema_full = FlightSchema()
def create_flight(data):
    """
    Creates a new flight using validated input data.
    """
    try:
        # Create the Flight object
        flight_inputs = flight_schema.load(data= data,session=db_session)
        print(flight_inputs)
        
        flight_search_result = get_flight_by_code(flight_inputs.flight_code)
        print(flight_search_result)
        if flight_search_result == None:
            # flight_inputs_sch = flight_schema_full.load(flight_inputs,session=db_session)
            db_session.add(flight_inputs)
            db_session.commit()
            return flight_schema_full.dump(flight_inputs)

        return flight_schema_full.dump(flight_search_result) 

    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None

def update_flight(data):
    try:
        flight = get_flight_by_code(data['flight_code'])
        if not flight:
            return None
        for key, value in data.items():
            setattr(flight, key, value)
        db_session.commit()
        print(flight)
        return flight_schema_full.dump(flight) 
    except Exception as e:
        print(e)
    return None



flight_schema_full_multi = FlightSchema(many=True)

def get_flight_by_code(flight_code = ''):
    return db_session.query(Flight).filter_by(flight_code = flight_code).first()


def get_flight_by_code_handler(flight_code = ''):
    return flight_schema_full.dump(get_flight_by_code(flight_code))

def get_flights_by_params(**kwargs):
    return flight_schema_full_multi.dump(db_session.query(Flight).filter_by(**kwargs).all())

from datetime import datetime,timedelta
def get_next_x_hours_flights(airport_code = '',hours = 4):
        print((datetime.now()+timedelta(hours=hours)).time(),type((datetime.now()+timedelta(hours=hours)).time()))
        val = db_session.query(Flight).where(Flight.source_airport_id == airport_code,Flight.departure_time<=(datetime.now()+timedelta(hours=hours)).time()).all()
        
        # 
        # print(val.departure_time <(datetime.now()+timedelta(hours=hours)).time())
        # print(val.departure_time,(datetime.now()+timedelta(hours=hours)).time())
        return flight_schema_full_multi.dump(val)
