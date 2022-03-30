class Account:

    def __init__(self, account_holder):

        self._holder = account_holder
        self._balance = 0
    
    @property
    def getHolder(self):
        return self._holder

    def deposit(self, amount):
        self._balance = self._balance - amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:  # if amount would exceed balance, decline
            return False
        self._balance = self._balance - amount
        return True


class LoanAccount(Account):

    def __init__(self, account_holder, balance, apr):
        self._holder = account_holder
        self._balance = balance
        self.apr = apr

    def deposit(self, amount):
        if amount > 0.1 * self._balance:
            self._balance = self._balance - amount + 5
            return False
        self._balance = self._balance - amount
        return True
        
    def process_month(self):
        self._balance = self._balance + self._balance * self.apr/1200
