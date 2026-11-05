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
def get_appointments_by_date(booked_on:str):
    response = functions.get_appointments_by_date(booked_on)
    if not booked_on.replace("-", "").isdigit():
        raise HTTPException(status_code=422, detail="Date must be written as YYYY-MM-DD")
    return response 

@app.get("/stats")                                         
def get_units():
    response = functions.get_units()
    return response

@app.get("/donors/eligible")                              
def get_eligible_donors(blood_group):
    response = functions.get_eligible_donors(blood_group)
    if blood_group not in functions.GROUPS:
        raise HTTPException(status_code=422 , detail="Blood group must be A+ , B+ ,O+ ,AB+ ,A- ,B- ,O- ,AB-")
    return response
