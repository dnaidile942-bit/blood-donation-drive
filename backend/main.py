
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import AM_functions 


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


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
