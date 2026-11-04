
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import AM_functions 


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/donors")
def donors(blood_group: str = None):
    return AM_functions.get_all_donors(blood_group=blood_group)

@app.post("/donors")
def add_donor(roll_no: str, name: str, blood_group: str, weight_kg: int):
    if blood_group not in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
        raise HTTPException(status_code=400, detail="Invalid blood group.")
    result = AM_functions.add_donor(roll_no=roll_no, name=name, blood_group=blood_group, weight_kg=weight_kg)
    if result is None:
        raise HTTPException(status_code=400, detail="Roll number already registered.")
    return result
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