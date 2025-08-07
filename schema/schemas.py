
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from models import *

# --------------------- AIRPORT ---------------------

class AirportSchema(SQLAlchemySchema):
    class Meta:
        model = Airport
        load_instance = True

    id = auto_field()
    name = auto_field()
    code = auto_field()
    location = auto_field()
    terminals = fields.Nested('TerminalOutputSchema', many=True)
    runways = fields.Nested('RunwayOutputSchema', many=True)

class AirportCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Airport
        load_instance = True

    name = auto_field()
    code = auto_field()
    location = auto_field()

class AirportOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Airport
        load_instance = True

    id = auto_field()
    name = auto_field()
    code = auto_field()
    location = auto_field()

# --------------------- AIRCRAFT ---------------------

class AircraftSchema(SQLAlchemySchema):
    class Meta:
        model = Aircraft
        load_instance = True

    id = auto_field()
    name = auto_field()
    capacity = auto_field()
    runway_distance = auto_field()

class AircraftCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Aircraft
        load_instance = True
        exclude = ('id',)

    name = auto_field()
    capacity = auto_field()
    runway_distance = auto_field()

class AircraftOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Aircraft
        load_instance = True

    id = auto_field()
    name = auto_field()
    capacity = auto_field()

# --------------------- AIRLINE COUNTER ---------------------

class AirlineCounterSchema(SQLAlchemySchema):
    class Meta:
        model = AirlineCounter
        load_instance = True

    id = auto_field()
    airline = auto_field()
    capacity = auto_field()
    status = auto_field()

class AirlineCounterCreateSchema(SQLAlchemySchema):
    class Meta:
        model = AirlineCounter
        load_instance = True
        exclude = ('id',)

    airline = auto_field()
    capacity = auto_field()
    status = auto_field()

class AirlineCounterOutputSchema(SQLAlchemySchema):
    class Meta:
        model = AirlineCounter
        load_instance = True

    id = auto_field()
    airline = auto_field()
    capacity = auto_field()
    status = auto_field()

# --------------------- AIRLINE STAFF ---------------------

class AirlineStaffSchema(SQLAlchemySchema):
    class Meta:
        model = AirlineStaff
        load_instance = True

    id = auto_field()
    name = auto_field()
    airline = auto_field()
    counter_id = auto_field()
    password = auto_field()

class AirlineStaffCreateSchema(SQLAlchemySchema):
    class Meta:
        model = AirlineStaff
        load_instance = True
        exclude = ('id',)

    name = auto_field()
    airline = auto_field()
    counter_id = auto_field()
    password = auto_field()

class AirlineStaffOutputSchema(SQLAlchemySchema):
    class Meta:
        model = AirlineStaff
        load_instance = True

    id = auto_field()
    name = auto_field()
    airline = auto_field()
    counter_id = auto_field()

# --------------------- AIRLINE ---------------------

class AirlineSchema(SQLAlchemySchema):
    class Meta:
        model = Airline
        load_instance = True

    id = auto_field()
    code = auto_field()
    base = auto_field()
    name = auto_field()

class AirlineCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Airline
        load_instance = True
        exclude = ('id',)

    code = auto_field()
    base = auto_field()
    name = auto_field()

class AirlineOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Airline
        load_instance = True

    id = auto_field()
    code = auto_field()
    name = auto_field()

# --------------------- AIRPORT STAFF ---------------------

class AirportStaffSchema(SQLAlchemySchema):
    class Meta:
        model = AirportStaff
        load_instance = True

    id = auto_field()
    name = auto_field()
    role = auto_field()
    terminal_id = auto_field()
    password = auto_field()

class AirportStaffCreateSchema(SQLAlchemySchema):
    class Meta:
        model = AirportStaff
        load_instance = True
        exclude = ('id',)

    name = auto_field()
    role = auto_field()
    terminal_id = auto_field()
    password = auto_field()

class AirportStaffOutputSchema(SQLAlchemySchema):
    class Meta:
        model = AirportStaff
        load_instance = True

    id = auto_field()
    name = auto_field()
    role = auto_field()

# --------------------- BAGGAGE BELT ---------------------

class BaggageBeltSchema(SQLAlchemySchema):
    class Meta:
        model = BaggageBelt
        load_instance = True

    id = auto_field()
    status = auto_field()
    capacity = auto_field()
    is_active = auto_field()
    terminal_id = auto_field()
    current_flight = auto_field()
    free_at = auto_field()

class BaggageBeltCreateSchema(SQLAlchemySchema):
    class Meta:
        model = BaggageBelt
        load_instance = True
        exclude = ('id',)

    status = auto_field()
    capacity = auto_field()
    is_active = auto_field()
    terminal_id = auto_field()
    current_flight = auto_field()
    free_at = auto_field()

class BaggageBeltOutputSchema(SQLAlchemySchema):
    class Meta:
        model = BaggageBelt
        load_instance = True

    id = auto_field()
    status = auto_field()
    capacity = auto_field()
    is_active = auto_field()

# --------------------- FLIGHT ---------------------

class FlightSchema(SQLAlchemySchema):
    class Meta:
        model = Flight
        load_instance = True

    id = auto_field()
    airline = auto_field()
    flight_code = auto_field()
    source_airport_id = auto_field()
    destination_id = auto_field()
    arrival_time = auto_field()
    departure_time = auto_field()
    aircraft_id = auto_field()

class FlightCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Flight
        load_instance = True
        exclude = ('id',)

    airline = auto_field()
    flight_code = auto_field()
    source_airport_id = auto_field()
    destination_id = auto_field()
    arrival_time = auto_field()
    departure_time = auto_field()
    aircraft_id = auto_field()

class FlightOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Flight
        load_instance = True

    id = auto_field()
    flight_code = auto_field()
    airline = auto_field()

# --------------------- FLIGHT INSTANCE ---------------------

class FlightInstanceSchema(SQLAlchemySchema):
    class Meta:
        model = FlightInstance
        load_instance = True

    id = auto_field()
    flight_id = auto_field()
    departure_time = auto_field()
    arrival_time = auto_field()
    gate_id = auto_field()
    baggage_belt_id = auto_field()
    passenger_count = auto_field()
    aircraft_id = auto_field()

class FlightInstanceCreateSchema(SQLAlchemySchema):
    class Meta:
        model = FlightInstance
        load_instance = True
        exclude = ('id',)

    flight_id = auto_field()
    departure_time = auto_field()
    arrival_time = auto_field()
    gate_id = auto_field()
    baggage_belt_id = auto_field()
    passenger_count = auto_field()
    aircraft_id = auto_field()

class FlightInstanceOutputSchema(SQLAlchemySchema):
    class Meta:
        model = FlightInstance
        load_instance = True

    id = auto_field()
    flight_id = auto_field()
    passenger_count = auto_field()

# --------------------- GATE BAGGAGE HISTORY ---------------------

class GateBaggageHistorySchema(SQLAlchemySchema):
    class Meta:
        model = GateBaggageHistory
        load_instance = True

    id = auto_field()
    entity_type = auto_field()
    entity_id = auto_field()
    timestamp = auto_field()
    performed_by = auto_field()
    action = auto_field()

class GateBaggageHistoryCreateSchema(SQLAlchemySchema):
    class Meta:
        model = GateBaggageHistory
        load_instance = True
        exclude = ('id',)

    entity_type = auto_field()
    entity_id = auto_field()
    timestamp = auto_field()
    performed_by = auto_field()
    action = auto_field()

class GateBaggageHistoryOutputSchema(SQLAlchemySchema):
    class Meta:
        model = GateBaggageHistory
        load_instance = True

    id = auto_field()
    entity_type = auto_field()
    action = auto_field()
    timestamp = auto_field()

# --------------------- PASSENGER ---------------------

class PassengerSchema(SQLAlchemySchema):
    class Meta:
        model = Passenger
        load_instance = True

    id = auto_field()
    name = auto_field()
    passport_number = auto_field()
    nationality = auto_field()
    boarding_pass_issued = auto_field()
    flight_instance_id = auto_field()

class PassengerCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Passenger
        load_instance = True
        exclude = ('id',)

    name = auto_field()
    passport_number = auto_field()
    nationality = auto_field()
    boarding_pass_issued = auto_field()
    flight_instance_id = auto_field()

class PassengerOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Passenger
        load_instance = True

    id = auto_field()
    name = auto_field()
    nationality = auto_field()

# --------------------- RUNWAY ---------------------

class RunwaySchema(SQLAlchemySchema):
    class Meta:
        model = Runway
        load_instance = True

    id = auto_field()
    identifier1 = auto_field()
    identifier2 = auto_field()
    length = auto_field()
    surface_type = auto_field()
    airport_id = auto_field()

class RunwayCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Runway
        load_instance = True
        exclude = ('id',)

    identifier1 = auto_field()
    identifier2 = auto_field()
    length = auto_field()
    surface_type = auto_field()
    airport_id = auto_field()

class RunwayOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Runway
        load_instance = True

    id = auto_field()
    identifier1 = auto_field()
    identifier2 = auto_field()
    surface_type = auto_field()
    length = auto_field()

# --------------------- TERMINAL ---------------------

class TerminalSchema(SQLAlchemySchema):
    class Meta:
        model = Terminal
        load_instance = True

    id = auto_field()
    number = auto_field()
    capacity = auto_field()
    status = auto_field()
    airport_id = auto_field()
    type = auto_field()

class TerminalCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Terminal
        load_instance = True

    number = auto_field()
    capacity = auto_field()
    status = auto_field()
    airport_id = auto_field()
    type = auto_field()

class TerminalOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Terminal
        load_instance = True

    id = auto_field()
    number = auto_field()
    status = auto_field()
    type = auto_field()

# --------------------- GATE ---------------------

class GateSchema(SQLAlchemySchema):
    class Meta:
        model = Gate
        load_instance = True

    id = auto_field()
    status = auto_field()
    capacity = auto_field()
    is_active = auto_field()
    terminal_id = auto_field()
    current_flight = auto_field()
    free_at = auto_field()

class GateCreateSchema(SQLAlchemySchema):
    class Meta:
        model = Gate
        load_instance = True
        exclude = ('id',)

    status = auto_field()
    capacity = auto_field()
    is_active = auto_field()
    terminal_id = auto_field()
    current_flight = auto_field()
    free_at = auto_field()

class GateOutputSchema(SQLAlchemySchema):
    class Meta:
        model = Gate
        load_instance = True

    id = auto_field()
    status = auto_field()
    capacity = auto_field()
    is_active = auto_field()
