
class Customers: 
    def __init__(self, f_name, l_name, ssn, phone_num, email, us_cit):
    # gathers customer personal info required to open an account.
        self.f_name = f_name
        self.l_name = l_name
        self.ssn = ssn
        self.phone_num = phone_num
        self.email = email
        self.us_cit = us_cit

    def change_info(self, current_info, new_info):
        if hasattr(self, current_info):
            setattr(self, current_info, new_info)
        else: 
            print(f"{current_info} in not a valid selection.")

class Address: 
    def __init__(self, street_address, city, zip):
    # gathers address info required to open account.
        self.self = self
        self.street_address = street_address
        self.city = city
        self.zip = zip


class DriversLicense: 
    def __init__(self, dl_num, state, exp_date, iss_date):
    # gathers info to open account concerning drivers license.
        self.dl_num = dl_num
        self.state = state
        self.exp_date = exp_date
        self.iss_date = iss_date
    
    def update_dl(self):
        pass