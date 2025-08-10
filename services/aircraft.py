from database import db_session  # your SQLAlchemy session setup
from sqlalchemy.exc import SQLAlchemyError
from schema.schemas import AircraftCreateSchema,AircraftSchema
aircraft_schema = AircraftCreateSchema()
aircraft_schema_full = AircraftSchema()
def create_aircraft(data):
    """
    Creates a new aircraft using validated input data.
    """
    try:
        # Create the Aircraft object
        aircraft_inputs = aircraft_schema.load(data= data,session=db_session)
        db_session.add(aircraft_inputs)
        db_session.commit()
        return aircraft_schema_full.dump(aircraft_inputs)


    except SQLAlchemyError as e:
        print(e)
        db_session.rollback()
    return None


js = [
  {
    "name": "Airbus A320",
    "capacity": 180,
    "runway_distance": 2100
  },
  {
    "name": "Boeing 737-800",
    "capacity": 189,
    "runway_distance": 2300
  },
  {
    "name": "Bombardier Q400",
    "capacity": 78,
    "runway_distance": 1400
  },
  {
    "name": "Embraer E175",
    "capacity": 88,
    "runway_distance": 1700
  },
  {
    "name": "Boeing 777-300ER",
    "capacity": 396,
    "runway_distance": 3000
  },
  {
    "name": "Airbus A350-900",
    "capacity": 325,
    "runway_distance": 2600
  },
  {
    "name": "ATR 72-600",
    "capacity": 70,
    "runway_distance": 1330
  },
  {
    "name": "Boeing 787-9",
    "capacity": 296,
    "runway_distance": 2800
  },
  {
    "name": "Airbus A320 Neo",
    "capacity": 190,
    "runway_distance": 2200
  },
  {
    "name": "McDonnell Douglas DC-10",
    "capacity": 380,
    "runway_distance": 3000
  }
]
def load_aircrafts():
    for i in js:
        print(create_aircraft(i))