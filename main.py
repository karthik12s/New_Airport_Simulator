from flask import Flask, render_template, request
from flask_socketio import  emit
from routes.airport import airport_blueprint
from routes.terminal import terminal_blueprint
from routes.airline import airline_blueprint
from routes.baggage import baggage_blueprint
from routes.runway import runway_blueprint
from routes.flight import flight_blueprint
from services.airport_manager import AirportManager

from real_time_events import socketio 

app = Flask(__name__)
socketio.init_app(app)
# Configure SocketIO
app.config['SECRET_KEY'] = 'secret' 

# Register blueprints
app.register_blueprint(airport_blueprint)
app.register_blueprint(terminal_blueprint)
app.register_blueprint(airline_blueprint)
app.register_blueprint(runway_blueprint)
app.register_blueprint(baggage_blueprint)
app.register_blueprint(flight_blueprint)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    print(f'Client Connected: {request.sid}')
    socketio.emit('server_message', {'data': 'Welcome to the Airport Simulator!'})

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client Disconnected: {request.sid}')

@socketio.on('client_message')
def handle_client_message(data):
    print('Received message from client:', data)
    emit('server_response', {'data': f'Server received: {data["message"]}'})

@app.route("/airport_operations")
def init_airport_operations():
    airport_manager = AirportManager(airport_code='fam')
    return {"message":"NA"}



# Run the SocketIO app
if __name__ == '__main__':
    print("Starting Flask-SocketIO server...")
    socketio.run(app, debug=True, port=5000)
    
