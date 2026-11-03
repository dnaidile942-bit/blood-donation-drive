from sqlalchemy import Integer, String, Column, ForeignKey, create_engine,Date;
from sqlalchemy.orm import Session, declarative_base;
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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
    last_donated_on = Column(Date,nullable = True)
    
    
   

class Appointment(Base):
    __tablename__="appointments"
    
    id = Column(Integer,primary_key = True)
    donor_id = Column(Integer, ForeignKey("donors.id"))
    drive_date = Column(Date)
    slot = Column(String)
    status = Column(String,default = "booked")
    booked_on = Column(Date,default = Date.now())
    
    
Base.metadata.create_all(engine)




def seed_data():
    session = Session(engine)
    today = date.today()

    if session.query(Donor).count() == 0:
        donor_records = [
            Donor(id=1,  roll_no="21BCE001", name="Aarav Sharma",  blood_group="A+",  weight_kg=68, last_donated_on=None),
            Donor(id=2,  roll_no="21BCE002", name="Diya Patel",    blood_group="O+",  weight_kg=55, last_donated_on=None),   
            Donor(id=3,  roll_no="21BCE003", name="Rohan Mehta",   blood_group="B+",  weight_kg=72, last_donated_on=None),
            Donor(id=4,  roll_no="21BCE004", name="Ananya Iyer",   blood_group="AB+", weight_kg=58, last_donated_on=None),
            Donor(id=5,  roll_no="21BCE005", name="Karthik Rao",   blood_group="O-",  weight_kg=80, last_donated_on=None),  
            Donor(id=6,  roll_no="21BCE006", name="Sneha Reddy",   blood_group="A-",  weight_kg=52, last_donated_on=None),   
            Donor(id=7,  roll_no="21BCE007", name="Vikram Singh",  blood_group="B-",  weight_kg=75, last_donated_on=None),
            Donor(id=8,  roll_no="21BCE008", name="Meera Nair",    blood_group="O+",  weight_kg=60, last_donated_on=None), 
            Donor(id=9,  roll_no="21BCE009", name="Arjun Das",     blood_group="AB-", weight_kg=70, last_donated_on=None),
            Donor(id=10, roll_no="21BCE010", name="Pooja Gupta",   blood_group="A+",  weight_kg=54, last_donated_on=None),  
            Donor(id=11, roll_no="21BCE011", name="Imran Khan",    blood_group="B+",  weight_kg=85, last_donated_on=None),
            Donor(id=12, roll_no="21BCE012", name="Lakshmi Menon", blood_group="O+",  weight_kg=57, last_donated_on=None),
        ]
        session.add_all(donor_records)
        session.commit()

    if session.query(Appointment).count() == 0:
        appointment_records = [
            # past donations (match last_donated_on above)
            Appointment(id=1,  donor_id=2,  drive_date=None,  slot="morning",   status="donated",   booked_on=today - timedelta(days=40)),
            Appointment(id=2,  donor_id=6,  drive_date=None,  slot="afternoon", status="donated",   booked_on=today - timedelta(days=55)),
            Appointment(id=3,  donor_id=10, drive_date=None,  slot="morning",   status="donated",   booked_on=today - timedelta(days=70)),
            Appointment(id=4,  donor_id=5,  drive_date=None, slot="morning",   status="donated",   booked_on=today - timedelta(days=130)),
            Appointment(id=5,  donor_id=8,  drive_date=None, slot="afternoon", status="donated",   booked_on=today - timedelta(days=210)),
            # past no-show
            Appointment(id=6,  donor_id=11, drive_date=None,  slot="afternoon", status="no_show",   booked_on=today - timedelta(days=40)),
            # upcoming bookings
            Appointment(id=7,  donor_id=1,  drive_date=None,   slot="morning",   status="booked",    booked_on=today),
            Appointment(id=8,  donor_id=3,  drive_date=None,   slot="morning",   status="booked",    booked_on=today),
            Appointment(id=9,  donor_id=4,  drive_date=None,   slot="afternoon", status="booked",    booked_on=today),
            # cancelled
            Appointment(id=10, donor_id=9,  drive_date=None,  slot="morning",   status="cancelled", booked_on=today),
        ]
        session.add_all(appointment_records)
        session.commit()

    session.close()


app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

seed_data()




