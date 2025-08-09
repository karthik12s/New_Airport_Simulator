from flask import Blueprint, request
from services import runway
from schema.schemas import RunwayCreateSchema,RunwayOutputSchema
from database import db_session
runway_blueprint = Blueprint('runway', __name__,
                        template_folder='templates')
runway_schema = RunwayCreateSchema()
runway_schema_full = RunwayOutputSchema()
@runway_blueprint.route('/create_runway',methods = ['POST'])
def create_runway():
    data = request.json
    return_runway = runway.create_runway(data=data)
    if return_runway:
        return return_runway,200
    return {"message":"Exception occured, Please retry"},200
    
@runway_blueprint.route('/get_runway',methods = ['POST'])
def get_runway():
    data = request.json
    try:
        return_airport = runway.get_runway_by_code_handler(data['code'])
        if return_airport:
            return return_airport,200
        return {"message":"Runway Not found"},200
    except Exception as e:
        return {"message":"Exception occured, Please retry"},200

@runway_blueprint.route("/update_runway",methods = ['POST'])
def update_runway():
    data = request.json
    return_runway = runway.update_runway(data)
    if return_runway:
        return {"message":"Update successfull","data":return_runway},200
    return {"message":"Update failed, Please retry"},200

@runway_blueprint.route("/get_runways")
def get_runways():
    try:
        airport_code = request.args.get("airport_id",default="",type=str)
        runways_result = runway.get_runways_by_airport(code=airport_code)
        if runways_result:
            print(list(runways_result))
            return {"message":"Fetch successful",'data':runways_result},200
        return {"message":"Couldn't get the Runways of given airport",'data':None},200
    except Exception as e:
        return {"message":"Fetch failed",'data':None},200