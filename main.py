from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import SU_functions

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SU_functions.seed_data()

@app.get("/donors")
def donors(blood_group: str = None):
    return SU_functions.get_all_donors(blood_group=blood_group)

@app.get("/donors/{roll_no}")
def get_donor(roll_no: str):
    donor = SU_functions.get_donor(roll_number=roll_no)
    if donor is None:
        raise HTTPException(status_code=404, detail="Donor not found.")
    return donor

@app.post("/donors")
def add_donor(roll_no, name, blood_group, weight_kg):  
    result = SU_functions.add_donor(roll_no=roll_no, name=name, blood_group=blood_group, weight_kg=weight_kg)
    if result == "duplicate":
        raise HTTPException(status_code=400, detail="Roll number already registered.")
    if result == "invalid_weight":
        raise HTTPException(status_code=422, detail="Weight must be between 50kg and 200kg.")
    if result == "invalid_blood_group":
        raise HTTPException(status_code=422, detail="Invalid blood group.")
    return result
