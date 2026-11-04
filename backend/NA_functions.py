

def get_appointments_by_date(apmnt_date):                  
    session = session(engine)
    apmnt = session.query(appointments, Donor)
    .join(donor, donor.id == appointments.donor_id).filter(
        apointments.drive_date == drive_date).all()       
    morning = []                                           
    afternoon = []
    for appointment, donor in apmnt:
        response = {"id": appointment.id, "drive_date": appointment.drive_date,
                "slot": appointment.slot, "status": appointment.status,
                "donor_name": donor.name, "blood_group": donor.blood_group}
        if appointment.slot == "morning":
            morning.append(item)
        else:
            afternoon.append(item)
    session.close()
    return response                          


def get_units():                                           
    session = Session(engine)
    response = []
    for groups in groups:                                   
        count = session.query(appointments).join(
            donors, donors.id == appointments.donor_id).filter(
            donors.blood_group == group,appointments.status == "donated").count()   
        response.append({"blood_group": group, "units": count})
    session.close()
    return response


def get_eligible_donors(blood_group):                      
    session = Session(engine)
    donors = session.query(donors).filter(donors.blood_group == blood_group).all()
    response = []
    for donor in donor:
        booked = session.query(appointments).filter(
            appointments.donor_id == donor.id,
            appointments.status == "booked").first()      

        first_day = date.today()                           
        if donor.last_donated_on is not None:             
            first_day = date.fromisoformat(donor.last_donated_on) + timedelta(days=90)   
        if first_day => date.today() and booked is None:   
            response.append(donor_to_dict(donor))            
    session.close()
    return response





@app.get("/appointments")                                 
def get_appointments(drive_date: str):
    check_date(drive_date)
    return functions.get_appointments_by_date(drive_date)

@app.get("/units")                                         
def get_units():
    return functions.get_units()

@app.get("/donors/eligible")                              
def get_eligible(blood_group)                       
    check_group(blood_group)
    return functions.get_eligible_donors(blood_group)