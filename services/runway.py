from sqlalchemy import and_, or_
from models import Runway
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import RunwayCreateSchema,RunwaySchema
runway_schema = RunwayCreateSchema()
runway_schema_full = RunwaySchema()
runway_schema_full_multi = RunwaySchema(many=True)
def create_runway(data):
    """
    Creates a new runway using validated input data.
    """
    try:
        # Create the Runway object
        print(data)
        runway_inputs = runway_schema.load(data= data,session=db_session)
        print(runway_inputs)
        runway_search_result = get_runway_by_airport_and_number(runway_inputs.airport_id,runway_inputs.identifier1)
        print(runway_search_result)
        if runway_search_result == None:
            print(runway_inputs)
            db_session.add(runway_inputs)
            db_session.commit()
            return runway_schema_full.dump(runway_inputs)

        return runway_schema_full.dump(runway_search_result) 

    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None

def update_runway(data):
    runway = get_runway_by_airport_and_number(airport_id=data['airport_id'],identifier1=data['identifier1'])
    if not runway:
        return None
    for key, value in data.items():
        setattr(runway, key, value)
    db_session.commit()
    return runway_schema_full.dump(runway)

def get_runway_by_airport_and_number(airport_id = '',identifier1=''):
    return db_session.query(Runway).filter(and_(Runway.airport_id == airport_id, or_(Runway.identifier1==identifier1,Runway.identifier2==identifier1))).first()

def get_runway_by_airport_and_number_handler(code,identifier1):
    return runway_schema_full.dump(get_runway_by_airport_and_number(code,identifier1))

def get_runways_by_airport(code):
    return runway_schema_full_multi.dump(db_session.query(Runway).filter_by(airport_id = code).all())