from flask import Flask
from routes.airport import airport_blueprint
from routes.terminal import terminal_blueprint
from routes.airline import airline_blueprint
from routes.baggage import baggage_blueprint
from routes.runway import runway_blueprint

app = Flask(__name__)

app.register_blueprint(airport_blueprint)
app.register_blueprint(terminal_blueprint)
app.register_blueprint(airline_blueprint)
app.register_blueprint(runway_blueprint)
app.register_blueprint(baggage_blueprint)
app.run(debug=True)

# from models.airport import Airport
# from models import terminal,airport_type,runway
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

# airport_instance = Airport(name = "Deccan Int Airport",code = "HYD",location = "Hyderabad")
# import os
# URL = f'{os.getenv("db_conn_string", "postgresql://postgres:postgres@localhost:5432/airport_db")}'
# print(URL,type(URL))
# engine = create_engine(str(URL))

# session = Session(bind=engine)

# session.add_all([airport_instance])
# session.commit()
# session.close()