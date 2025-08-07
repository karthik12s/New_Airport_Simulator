from models import Airport
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import AirportCreateSchema,AirportSchema
airport_schema = AirportCreateSchema()
airport_schema_full = AirportSchema()
def create_airport(data):
    """
    Creates a new airport using validated input data.
    """
    try:
        # Create the Airport object
        airport_inputs = airport_schema.load(data= data,session=db_session)
        airport_search_result = get_airport_by_code(airport_inputs.code)
        if airport_search_result == None:
            db_session.add(airport_inputs)
            db_session.commit()
            return airport_schema_full.dump(airport_inputs)

        return airport_schema_full.dump(airport_search_result) 

    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None

def update_airport(airport_id, **kwargs):
    airport = db_session.query(Airport).filter_by(id=airport_id).first()
    if not airport:
        return None
    for key, value in kwargs.items():
        setattr(airport, key, value)
    db_session.commit()
    return airport

def get_airport_by_code(code):
    return db_session.query(Airport).filter_by(code=code).first()

def get_airport_by_code_handler(code):
    return airport_schema_full.dump(get_airport_by_code(code))