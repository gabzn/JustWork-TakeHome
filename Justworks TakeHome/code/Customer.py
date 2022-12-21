from collections import defaultdict
import datetime as dt
from MonthYearTransaction import MonthYearTransaction

class Customer:
    def __init__(self, id, transactions):
        self.id = id
        
        self.transaction_dict = defaultdict(MonthYearTransaction)
        self.process_transactions(transactions)
    
    def process_transactions(self, transactions):
        for (index, date, amount) in transactions.itertuples():
            month_year = (date.month, date.year)
            self.transaction_dict[month_year].apply(amount)
            
    def generate_report(self):
        report = []
        for (month, year), transaction in self.transaction_dict.items():
            date_object = dt.datetime(year, month, 1)
            report.append([self.id, date_object.strftime('%m/%Y'), transaction.get_min_balance(), transaction.get_max_balance(), transaction.get_balance()])
        
        return report