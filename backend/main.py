from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import NA_functions 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/appointments")                                 
def get_appointments_by_date(drive_date:str):
    response = NA_functions.get_appointments_by_date(drive_date)
    return response 
@app.get("/appointments/status/units")                                         
def get_units():
    response = NA_functions.get_units()
    return response
@app.get("/donors/eligible")                              
def get_eligible_donors(blood_group:str):
    response = NA_functions.get_eligible_donors(blood_group)
    return response
