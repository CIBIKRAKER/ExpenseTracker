import datetime

class Expense:

    def __init__(self, description: str, amount: float, category: str):
        self.id = 1
        self.description = description
        self.amount = amount
        self.date =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category

    def __str__(self):
        print(f"Expense[ID: {self.id}, Description: {self.description}, Amount: {self.amount}, Date: {self.date}, Category: {self.category}]")    
