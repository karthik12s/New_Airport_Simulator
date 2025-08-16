import time
from datetime import datetime,timedelta
from models import Flight,FlightInstance,Gate,BaggageBelt as Baggage
from database import db_session
from schema.schemas import FlightSchema,FlightInstanceCreateSchema,FlightInstanceSchema,GateSchema
from sqlalchemy import or_,exists, update

flight_full_schema = FlightSchema(many = True)
flight_instance_create_schema = FlightInstanceCreateSchema()
flight_instance_schema = FlightInstanceSchema(many = True)
gates_schema = GateSchema(many = True)
class AirportManager():
    def __init__(self,airport_code):
        self.airport_code = airport_code
        # self.add_recurring_flights(hours=4)
        # while(1):
        #     self.add_recurring_flights(hours=4)
        #     time.sleep(900)
        # self.auto_assign_gates()
        self.listen_from_gate()
    def add_recurring_flights(self,hours = 4):
        # This module to be run on 15 minutes once basis
        # Get all the Flights that are recurring and scheduled in next 4 hours 
        # Create Flight Instance for each flight and add them to queue
        new_time = datetime.utcnow() + timedelta(hours = hours)
        # To check if there is a midnight case that we need to handle
        if(datetime.utcnow().time().hour>=24-hours):
            # If we are also fetching flights for early morning tomorrow
            new_flights = db_session.query(Flight).filter(
            Flight.source_airport_id == self.airport_code,
            or_(Flight.departure_time > datetime.utcnow().time(),
            Flight.departure_time < new_time.time()),
            Flight.recurring == True,
            ~exists().where(
                (FlightInstance.flight_id == Flight.id) & 
                (FlightInstance.departure_time > datetime.utcnow().time()) 
            )
            ).all()
            
        else:
            print(datetime.utcnow())
            new_flights = db_session.query(Flight).filter(
            Flight.source_airport_id == self.airport_code,
            Flight.departure_time < new_time.time(),
            Flight.recurring == True,
            ~exists().where(
                (FlightInstance.flight_id == Flight.id) & 
                (FlightInstance.departure_time > new_time) 
            )
            ).all()

        print(new_flights)

        for new_flight in new_flights:
            # Generation of date for Flights
            arr_datetime = datetime.combine(datetime.utcnow(),new_flight.arrival_time)
            dep_datetime = datetime.combine(datetime.utcnow(),new_flight.departure_time)

            #If the flight is scheduled for tomorrow
            if dep_datetime<datetime.utcnow():
                dep_datetime = dep_datetime + timedelta(days=1)
                arr_datetime = arr_datetime + timedelta(days=1)
            
            #If the flight starts today but ends tomorrow
            if dep_datetime.time()>arr_datetime.time():
                arr_datetime = arr_datetime + timedelta(days=1)
            
            # Creation of New flight instance

            new_instance = FlightInstance(
                flight_id = new_flight.id,
                departure_time = dep_datetime,
                arrival_time = arr_datetime,
                gate_id = None,
                baggage_belt_id = None,
                passenger_count = 120,
                aircraft_id =  new_flight.aircraft_id,
                
                source_airport_id = new_flight.source_airport_id,
                
                destination_id = new_flight.destination_id,
                airline = new_flight.airline,
                flight_code = new_flight.flight_code,
                state = "NA"
            )

            db_session.add(new_instance)
            db_session.commit()

    def auto_assign_gates(self):
        # Get the virtual queue from db for flights waiting for gates
        # Assign gates for the flights and increase their dep time if gates aren't available
        waiting_flights = db_session.query(FlightInstance).filter(FlightInstance.state == "NA",FlightInstance.source_airport_id == self.airport_code).order_by(FlightInstance.departure_time).all()
        current_gates = db_session.query(Gate).filter(or_(Gate.free_at<=datetime.utcnow(),Gate.free_at==None),Gate.is_active==True).order_by(Gate.free_at).all()
        
        #Process waiting Flights

        for i in range(len(waiting_flights)):
            if len(current_gates)==0:
                departure_time_inc = []
                departure_time_inc_codes = []
                for flight in waiting_flights[i:]:
                    departure_time_inc.append(flight.id)
                    departure_time_inc_codes.append(flight.flight_code)

                update_stmt = update(FlightInstance).where(FlightInstance.id in departure_time_inc).values(departure_time=FlightInstance.departure_time + timedelta(minutes=15))
                db_session.execute(update_stmt)
                db_session.commit()
                print(f"Flights {','.join(departure_time_inc_codes)} rescheduled")
                
            else:
                free_time = waiting_flights[i].departure_time
                if waiting_flights[i].departure_time < datetime.utcnow()+timedelta(minutes = 40):
                    update_stmt = update(FlightInstance).where(FlightInstance.id == waiting_flights[i].id).values(departure_time=FlightInstance.departure_time + datetime.utcnow()+timedelta(minutes = 40)-free_time)
                update_stmt = update(Gate).where(Gate.id == current_gates[0].id).values(current_flight = waiting_flights[i].flight_code,free_at=waiting_flights[i].departure_time)

                db_session.execute(update_stmt)
                update_stmt = update(FlightInstance).where(FlightInstance.id == waiting_flights[i].id).values(state = "GATE",gate_id = current_gates[0].id)
                db_session.execute(update_stmt)
                db_session.commit()
                
                print(f"Gate {current_gates[0].number} assigned to flight {waiting_flights[i].flight_code}")
                current_gates.pop(0)


    def auto_assign_baggages(self):
        # Get the virtual queue from db for flights waiting for baggage
        # Assign baggages for the flights and increase their arr time if baggagebelts aren't available
        waiting_flights = db_session.query(FlightInstance).filter(FlightInstance.state == ["ARR","TAXI"],FlightInstance.destination_id==self.airport_code).order_by(FlightInstance.departure_time).all()
        current_baggages = db_session.query(Gate).filter(or_(Baggage.free_at<=datetime.utcnow(),Baggage.free_at==None),Baggage.is_active==True).order_by(Baggage.free_at).all()
        
        #Process waiting Flights

        for i in range(len(waiting_flights)):
            if len(current_baggages)==0:
                arrival_time_inc = []
                arrival_time_inc_codes = []
                for flight in waiting_flights[i:]:
                    arrival_time_inc.append(flight.id)
                    arrival_time_inc_codes.append(flight.flight_code)

                # update_stmt = update(FlightInstance).where(FlightInstance.id in arrival_time_inc).values(arrival_time=FlightInstance.arrival_time + timedelta(minutes=15))
                # db_session.execute(update_stmt)
                # db_session.commit()
                print(f"Flights {','.join(arrival_time_inc_codes)} Waiting for Baggage")
                
            else:
                free_time = waiting_flights[i].arrival_time
                # if waiting_flights[i].arrival_time < datetime.utcnow()+timedelta(minutes = 40):
                #     update_stmt = update(FlightInstance).where(FlightInstance.id == waiting_flights[i].id).values(arrival_time=FlightInstance.arrival_time + datetime.utcnow()+timedelta(minutes = 40)-free_time)
                update_stmt = update(Baggage).where(Baggage.id == current_baggages[0].id).values(current_flight = waiting_flights[i].flight_code,free_at=waiting_flights[i].arrival_time)

                db_session.execute(update_stmt)
                update_stmt = update(FlightInstance).where(FlightInstance.id == waiting_flights[i].id).values(state = "baggage")
                
                db_session.execute(update_stmt)
                db_session.commit()
                
                print(f"Baggage {current_baggages[0].number} assigned to flight {waiting_flights[i].flight_code}")
                current_baggages.pop(0)

    def atc_handover():
        # update the state of the aircraft if the gate is closed and handover to atc for taxi clearance
        pass

    def listen_from_atc():
        # get the state of aircraft that are on the taxiway and redirect t auto assign baggages
        pass
    
    def listen_from_gate(self):
        # get the latest updates on the gate closure by talking to airline about flight
        # if gate is getting closed as expected update its state and redirect to atc_handover
        current_flights = db_session.query(FlightInstance,Gate).filter(FlightInstance.state == "GATE").join(Gate).all()
        print(current_flights)
        for flight in current_flights:
            
            if flight[0].departure_time < datetime.utcnow():
                print(f"Gate {flight[1].number}  is being closed ")
                update_stmt = update(FlightInstance).where(FlightInstance.id == flight[0].id).values(state = "PUSHBACK")
                db_session.execute(update_stmt)
                db_session.commit()
                print(f"Gate {flight[1].number}  is closed ")
