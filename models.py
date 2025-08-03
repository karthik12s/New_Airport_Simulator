
from sqlalchemy import (
    DATETIME, TIME, Boolean, DateTime, ForeignKey, Integer, Column, Integer, String
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Airport(Base):
    __tablename__ = 'airport'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    code = Column(String, unique=True)
    location = Column(String)
    terminals = relationship('Terminal', back_populates='airport')
    # types = relationship('AirportType', secondary=airport_airport_type, back_populates='airports')
    runways = relationship("Runway", back_populates="airport")

class Aircraft(Base):
    __tablename__ = 'aircraft'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    capacity = Column(Integer)
    runway_distance = Column(Integer)

class AirlineCounter(Base):
    __tablename__ = 'airline_counter'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    airline = Column(String)
    capacity = Column(Integer)
    status = Column(String)

class AirlineStaff(Base):
    __tablename__ = 'airline_staff'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    airline = Column(String)
    counter_id = Column(UUID(as_uuid=True), ForeignKey('airline_counter.id'))
    password = Column(String)

class Airline(Base):
    __tablename__ = "airlines"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    base = Column(String, nullable=False)
    name = Column(String,nullable=False)
    def __repr__(self):
        return f"<Airline(code={self.code}, base={self.base})>"

class AirportStaff(Base):
    __tablename__ = 'airport_staff'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    role = Column(String)
    terminal_id = Column(UUID(as_uuid=True), ForeignKey('terminal.id'))
    password = Column(String)

class BaggageBelt(Base):
    __tablename__ = 'baggage_belt'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(String)
    capacity = Column(Integer)
    is_active = Column(Boolean)
    terminal_id = Column(UUID(as_uuid=True), ForeignKey('terminal.id'))
    terminal = relationship('Terminal',back_populates = 'baggages')
    current_flight = Column(UUID(as_uuid=True), ForeignKey('flight.id'))
    free_at = Column(DATETIME)

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    airline = Column(String)
    flight_code = Column(String)
    source = relationship('Airport')
    source_airport_id = Column(UUID(as_uuid=True), ForeignKey('airport.id'))
    destination = relationship('Airport')
    destination_id = Column(UUID(as_uuid=True), ForeignKey('airport.id'))
    arrival_time = Column(TIME)
    departure_time = Column(TIME)
    aircraft_id = Column(UUID(as_uuid=True), ForeignKey('aircraft.id'))
    aircraft = relationship('Aircraft')
    
class FlightInstance(Base):
    __tablename__ = 'flight_instance'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    flight_id = Column(UUID(as_uuid=True), ForeignKey('flight.id'))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    gate_id = Column(UUID(as_uuid=True), ForeignKey('gate.id'))
    baggage_belt_id = Column(UUID(as_uuid=True), ForeignKey('baggage_belt.id'))
    flight = relationship('Flight')
    gate = relationship('Gate')
    baggage_belt = relationship('BaggageBelt')
    passenger_count = Column(Integer)
    aircraft_id = Column(UUID(as_uuid=True), ForeignKey('aircraft.id'))
    aircraft = relationship('Aircraft')

class GateBaggageHistory(Base):
    __tablename__ = 'gate_baggage_history'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_type = Column(String)  # 'gate' or 'baggage'
    entity_id = Column(UUID(as_uuid=True))
    timestamp = Column(DateTime)
    action = Column(String)
    performed_by = Column(UUID(as_uuid=True), ForeignKey('airport_staff.id'))


class Passenger(Base):
    __tablename__ = 'passenger'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    passport_number = Column(String)
    nationality = Column(String)
    boarding_pass_issued = Column(Boolean)
    flight_instance_id = Column(UUID(as_uuid=True), ForeignKey('flight_instance.id'))
    flight_instance = relationship('FlightInstance')


class Runway(Base):
    __tablename__ = "runways"

    id = Column(Integer, primary_key=True)
    identifier1 = Column(String, nullable=False)
    identifier2 = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    surface_type = Column(String, nullable=False)
    airport_id = Column(UUID(as_uuid=True), ForeignKey('airport.id'))
    airport = relationship('Airport',back_populates = "runways")


    def __repr__(self):
        return f"<Runway(identifier={self.identifier}, length={self.length}, surface_type={self.surface_type})>"

class Terminal(Base):
    __tablename__ = 'terminal'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    number = Column(String)
    capacity = Column(Integer)
    status = Column(String)
    airport_id = Column(UUID(as_uuid=True), ForeignKey('airport.id'))
    airport = relationship('Airport',back_populates = 'terminals')
    type = Column(String)
    gates = relationship('Gate', back_populates='terminal')
    baggages = relationship('BaggageBelt',back_populates='terminal')
