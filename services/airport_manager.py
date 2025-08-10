class AirportManager():
    def __init__(self,airport_code):
        self.airport_code = airport_code
    
    def add_recurring_flights():
        # This module to be run on 15 minutes once basis
        # Get all the Flights that are recurring and scheduled in next 4 hours 
        # Create Flight Instance for each flight and add them to queue
        pass

    def auto_assign_gates():
        # Get the virtual queue from db for flights waiting for gates
        # Assign gates for the flights and increase their dep time if gates aren't available
        pass

    def auto_assign_baggages():
        # Get the virtual queue from db for flights waiting for baggage
        # Assign gates for the flights and increase their arr time if baggagebelts aren't available
        pass

    def atc_handover():
        # update the state of the aircraft if the gate is closed and handover to atc for taxi clearance
        pass

    def listen_from_atc():
        # get the state of aircraft that are on the taxiway and redirect t auto assign baggages
        pass
    
    def listen_from_gate():
        # get the latest updates on the gate closure by talking to airline about flight
        # if gate is getting closed as expected update its state and redirect to atc_handover
        pass

    
    