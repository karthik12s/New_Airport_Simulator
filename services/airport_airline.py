from models import AirportAirlineMapping
from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import AirportAirlineMappingSchema

airport_airline_mapping_schema  = AirportAirlineMappingSchema()

def create_airport_airline_mapping(data):
    """
    Creates a new Airport Airline Mapping using validated input data.
    """
    try:
        # Create the Airport object
        airport_airline_mapping_inputs = airport_airline_mapping_schema.load(data= data,session=db_session)
        airport_airline_mapping_search_result = get_airport_airline_by_code(airport_airline_mapping_inputs.airport,airport_airline_mapping_inputs.airline)
        if airport_airline_mapping_search_result == None:
            db_session.add(airport_airline_mapping_inputs)
            db_session.commit()
            return airport_airline_mapping_schema.dump(airport_airline_mapping_inputs)

        return airport_airline_mapping_schema.dump(airport_airline_mapping_search_result) 

    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None

def update_airport_airline_mapping(data):
    try:
        airport_airline_mapping_search_result = get_airport_airline_by_code(data["airport"],data['airline'])
        if not airport_airline_mapping_search_result:
            return None
        for key, value in data.items():
            setattr(airport_airline_mapping_search_result, key, value)
        db_session.commit()
        return airport_airline_mapping_search_result
    except Exception as e:
        print(e)
    return None

def get_airport_airline_by_code(airport_code,airline_code):
    return db_session.query(AirportAirlineMapping).filter_by(airport = airport_code,airline = airline_code).first()

def get_airport_airline_by_code_handler(airport_code,airline_code):
    return airport_airline_mapping_schema.dump(get_airport_airline_by_code(airline_code,airline_code))