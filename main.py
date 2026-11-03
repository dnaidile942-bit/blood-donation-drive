from fastapi import FastAPI,HTTPException
import functions

app = FastAPI()

@app.get("/donors")
def donors():
    return functions.get_all_donors()

@app.get("/donor/{roll_number}")
def donor(roll_number):
    return functions.get_donor(roll_number=roll_number)

@app.post("/item")
def donor(roll_no,name,blood_group,weight,last_donated_on):
    return functions.add_donor(roll_no=roll_no,name=name,blood_group=blood_group,weight=weight,last_donated_on=last_donated_on)

