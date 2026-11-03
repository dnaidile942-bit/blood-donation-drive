def get_all_donors():
    sesssion = Session(engine)
    donors = session.query(blood).all()
    response = []
    for donors in donors:
        temp_donor = {
            "id":donor.id,
            "roll_no":donor.roll_no,
            "name":donor.name,
            "blood_group":donor.blood_group,
            "weight":donor.weight,
            "last_donated_on":donor.last_donated_on,

        }
        response.append(temp_donor)
        session.close()
        return response

def get_donor(roll_number):
    session = Session(engine)
    donor=session.get(donor,roll_number)
    response = {
        "id":donor.id,
        "roll_no":donor.roll_no,
        "name":donor.name,
        "blood_group":donor.blood_group,
        "weight":donor.weight,
        "last_donated_on":donor.last_donated_on,
    }  
    session.close()
    return response

def add_donor(roll_no,name,blood_group,weight,last_donated_on):
    session = Session(engine)
    donor = donors(roll_no=roll_no,name=name,blood_group=blood_group,weight=weight,last_donated_on=last_donated_on)
    session.add(donor)
    response = {
        "id":donor.id,
        "roll_no":donor.roll_no,
        "name":donor.name,
        "blood_group":donor.blood_group,
        "weight":donor.weight,
        "last_donated_on":donor.last_donated_on,

    }
    session.commit()
    session.close()
    return response


    
         




