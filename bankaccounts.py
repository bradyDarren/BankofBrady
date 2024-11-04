
class Account:
    def __init__(self, acct_num, acct_balance):
        self.acct_num = acct_num
        self.acct_balance = acct_balance

class Checkings(Account): 
    def __init__(self, checking_bal):
        super().__init__
        self.checking_bal = checking_bal

    def get_check_bal(self, checking_bal):
        return f"The balacne of our Checking account is ${float(checking_bal)}."

class Savings: 
    def __init__(self):
        pass
    
    def get_save_bal(self):
        pass

class CreditCard: 
    def __init__(self):
        pass

    def cc_interest(self):
        pass

class AutoLoan: 
    def __init__(self):
        pass

    def auto_interest(self):
        pass

class MortageLoan:
    def __init__(self):
        pass
