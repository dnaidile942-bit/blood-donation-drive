from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import AM_functions 
import SU_functions
import NA_functions

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#E1 GET all donors
@app.get("/donors")
def donors(blood_group: str = None):
    return SU_functions.get_all_donors(blood_group=blood_group)

#E8 GET eligible donors by blood group
@app.get("/donors/eligible")                              
def get_eligible_donors(blood_group:str):
    response = NA_functions.get_eligible_donors(blood_group)
    return response


#E2 GET DONORS by roll number
@app.get("/donors/{roll_no}")
def get_donor(roll_no: str):
    return SU_functions.get_donor(roll_no.upper())

#E3 Add donor
@app.post("/donors")
def add_donor(roll_no: str, name: str, blood_group: str, weight_kg: int):
    return SU_functions.add_donor(roll_no=roll_no, name=name, blood_group=blood_group, weight_kg=weight_kg)

#E4 Book appointment
@app.post("/appointments")
def book_appoint(roll_no: str, drive_date: str, slot: str):
    return AM_functions.book_appoint(roll_no.upper(), drive_date, slot.lower())

#E5 Cancel appointment
@app.patch("/appointments/{id}/cancel")
def cancel_appoint(id: int):
    return AM_functions.cancel_appoint(id)

#E6 Mark appointment
@app.patch("/appointments/{id}/status")
def mark_appoint(id: int, status: str ):
    return AM_functions.mark_appoint(id, status.lower())

#E7 GET appointments by date
@app.get("/appointments") 
def get_appointments(drive_date:str):
    response = NA_functions.get_appointments_by_date(drive_date)
    return response 

#E9 GET units donated by blood group
@app.get("/appointments/status/units")                                         
def get_units():
    response = NA_functions.get_units()
    return response

