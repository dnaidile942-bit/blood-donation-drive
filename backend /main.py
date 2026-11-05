import SU_functions

#E1 GET all donors
@app.get("/donors")
def donors(blood_group: str = None):
    return SU_functions.get_all_donors(blood_group=blood_group)


#E2 GET DONORS by roll number
@app.get("/donors/{roll_no}")
def get_donor(roll_no: str):
    return SU_functions.get_donor(roll_no.upper())

#E3 Add donor
@app.post("/donors")
def add_donor(roll_no: str, name: str, blood_group: str, weight_kg: int):
    return SU_functions.add_donor(roll_no=roll_no, name=name, blood_group=blood_group, weight_kg=weight_kg)
