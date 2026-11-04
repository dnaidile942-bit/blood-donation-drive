from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import functions 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/appointments")                                 
def get_appointments_by_date(Appointment):
    response = functions.get_appointments_by_date(Appointment)
    return response 

@app.get("/units")                                         
def get_units():
    response = functions.get_units()
    return response

@app.get("/donors/eligible")                              
def get_eligible_donors(blood_group):
    response = functions.get_eligible_donors(blood_group)
    return response