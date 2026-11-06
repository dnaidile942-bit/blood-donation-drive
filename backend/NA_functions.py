from sqlalchemy import Integer, String, Column, ForeignKey, create_engine,Date,func
from sqlalchemy.orm import Session, declarative_base
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from datetime import date,datetime,timedelta

GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

DB_PATH = "blooddrive.db"

engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()


class Donor(Base):
    __tablename__="donors"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    roll_no = Column(String,unique = True)
    blood_group = Column(String)
    weight_kg = Column(Integer)
    last_donated_on = Column(Date)
    
    
   

class Appointment(Base):
    __tablename__="appointments"
    
    id = Column(Integer,primary_key = True)
    donor_id = Column(Integer, ForeignKey("donors.id"))
    drive_date = Column(Date)
    slot = Column(String)
    status = Column(String,default = "booked")
    booked_on = Column(Date,default = func.current_date())
    
    
Base.metadata.create_all(engine)

 
def get_appointments_by_date(drive_date):
    if len(drive_date) != 10 or drive_date[4] != "-" or drive_date[7] != "-":
            raise HTTPException(status_code=422, detail="Date must be written as YYYY-MM-DD")
    drive_date = datetime.strptime(drive_date, "%Y-%m-%d").date()

    session = Session(engine)
    response = []

    
    for slot in ["morning", "afternoon"]:
        apointsday = session.query(Appointment).filter(
            Appointment.drive_date == drive_date,
            Appointment.slot == slot
        ).all()

        for apoint in apointsday:
            if apoint.status == "booked":
                donor = session.get(Donor, apoint.donor_id)
                response.append({
                    "id": apoint.id,
                    "donor_id": donor.id,
                    "name": donor.name,
                    "blood_group": donor.blood_group,
                    "drive_date": apoint.drive_date,
                    "slot": apoint.slot,
                    "status": apoint.status,
                })

    session.close()
    return response

def get_units():                                           
    session = Session(engine)

    unitscounts = {}
    for g in GROUPS:
        unitscounts[g] = 0

    donated = session.query(Appointment).filter(Appointment.status=="donated").all()

    for donate in donated:                                   
        donor = session.get(Donor , donate.donor_id)   
        unitscounts[donor.blood_group] +=1

    session.close()
    return unitscounts

def get_eligible_donors(blood_group):
    blood_group=blood_group.upper() 
    if blood_group not in GROUPS:
            raise HTTPException(status_code=422 , detail="Blood group must be A+ , B+ ,O+ ,AB+ ,A- ,B- ,O- ,AB-")                    
    session = Session(engine)
    donors = session.query(Donor).filter(Donor.blood_group == blood_group).all()
    response = []
    for donor in donors :
        booked = session.query(Appointment).filter(
            Appointment.donor_id == donor.id,
            Appointment.status == "booked").first()      
        eligible_day = date.today()                           
        if donor.last_donated_on is not None:             
            eligible_day = donor.last_donated_on + timedelta(days=90)   
        if eligible_day <= date.today() and booked is None:   
            response.append({              
                "name": donor.name,
                "roll_no": donor.roll_no,
                "blood_group": donor.blood_group,
                "weight_kg": donor.weight_kg,
                "last_donated_on": donor.last_donated_on})         
    session.close()
    return response
