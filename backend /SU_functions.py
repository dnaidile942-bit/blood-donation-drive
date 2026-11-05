import SU_functions

def get_all_donors(blood_group=None):
    session = Session(engine)
    if blood_group is not None:
            blood_group = blood_group.upper()
            if blood_group not in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
                session.close()
                raise HTTPException(status_code=422, detail="Invalid blood group.")

    if blood_group is None:
        donors = session.query(Donor).all()
    else:
        blood_group = blood_group.upper()
        donors = session.query(Donor).filter(Donor.blood_group == blood_group).all()

    response = []
    for donor in donors:
        apoint = session.query(Appointment).filter(Appointment.donor_id == donor.id).first()
        if apoint is None:
            status = None
            drive_date = None
        else:
            status = apoint.status
            drive_date = apoint.drive_date
        temp_donor = {
            "id": donor.id,
            "roll_no": donor.roll_no,
            "name": donor.name,
            "blood_group": donor.blood_group,
            "weight_kg": donor.weight_kg,
            "last_donated_on": donor.last_donated_on,
            "status":status,
            "drive_date":drive_date
        }
        response.append(temp_donor)

    session.close()
    return response


def get_donor(roll_no):
    
    session = Session(engine)

    donor = session.query(Donor).filter(Donor.roll_no == roll_no).first()
    if donor is None:
        session.close()
        raise HTTPException(status_code=404, detail="Donor not found")

    appoints = session.query(Appointment).filter(Appointment.donor_id == donor.id).all()
    appoint_list = []
    for apoint in appoints:
        appoint_list.append({
            "id": apoint.id,
            "drive_date": apoint.drive_date,
            "slot": apoint.slot,
            "status": apoint.status,
            "booked_on": apoint.booked_on,
        })

    response = {
        "id": donor.id,
        "roll_no": donor.roll_no,
        "name": donor.name,
        "blood_group": donor.blood_group,
        "weight_kg": donor.weight_kg,
        "last_donated_on": donor.last_donated_on,
        "appointments": appoint_list,
    }

    session.close()
    return response


def add_donor(roll_no, name, blood_group, weight_kg):
    roll_no = roll_no.upper()
    blood_group = blood_group.upper()

    if blood_group not in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
        raise HTTPException(status_code=422, detail="Invalid blood group.")
    if weight_kg < 50 or weight_kg > 200:
        raise HTTPException(status_code=422, detail="Weight must between  50kg to 200kg.")

    session = Session(engine)

    donorexi = session.query(Donor).filter(Donor.roll_no == roll_no).first()
    if donorexi is not None:
        session.close()
        raise HTTPException(status_code=400, detail="Roll number already registered.")

    donor = Donor(roll_no=roll_no, name=name, blood_group=blood_group, weight_kg=weight_kg)
    session.add(donor)
    session.commit()
    
    response = {
        "id": donor.id,
        "roll_no": donor.roll_no,
        "name": donor.name,
        "blood_group": donor.blood_group,
        "weight_kg": donor.weight_kg,
        "last_donated_on": donor.last_donated_on,
    }

    session.close()
    return response
