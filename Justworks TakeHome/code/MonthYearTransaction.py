import math

class MonthYearTransaction:
    def __init__(self):
        self.balance = 0
        self.min_balance = math.inf
        self.max_balance = -math.inf

    def apply(self, amount):
        self.balance += amount
        self.min_balance = min(self.min_balance, self.balance)
        self.max_balance = max(self.max_balance, self.balance)
    
    def get_balance(self):
        return self.balance
    
    def get_min_balance(self):
        return self.min_balance
    
    def get_max_balance(self):
        return self.max_balance