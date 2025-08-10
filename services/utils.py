

from sqlalchemy import update
from models import BaggageBelt,Gate
from database import db_session

def bulk_update_baggage_status(status,terminal_id):
    print(terminal_id,status)
    stmt = (
        update(BaggageBelt)
        .where(BaggageBelt.terminal_id == terminal_id)
        .values(is_active=status)
    )
    result = db_session.execute(stmt)
    print(result)
    db_session.commit()
    if result:
        print(result)
        return {"message":"Updated successfully"}
    return None

def bulk_update_gate_status(status,terminal_id):
    print(terminal_id,status)
    stmt = (
        update(Gate)
        .where(Gate.terminal_id == terminal_id)
        .values(is_active=status)
    )
    result = db_session.execute(stmt)
    print(result)
    db_session.commit()
    if result:
        print(result)
        return {"message":"Updated successfully"}
    return None