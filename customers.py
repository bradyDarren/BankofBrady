
class Customers: 
    def __init__(self, f_name, l_name, ssn, phone_num, email, us_cit):
    # gathers customer personal info required to open an account.
        self.f_name = f_name
        self.l_name = l_name
        self.ssn = ssn
        self.phone_num = phone_num
        self.email = email
        self.us_cit = us_cit

    
    def name_change(self):
    # made to take into account marital name changes.
        pass

class Address: 
    def __init__(self, street_address, city, zip):
    # gathers address info required to open account.
        self.self = self
        self.street_address = street_address
        self.city = city
        self.zip = zip
    
    def address_change(self):
        pass 

class DriversLicense: 
    def __init__(self, dl_num, state, exp_date, iss_date):
    # gathers info to open account.
        self.dl_num = dl_num
        self.state = state
        self.exp_date = exp_date
        self.iss_date = iss_date
    
    def update_dl(self):
        pass