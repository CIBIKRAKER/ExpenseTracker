import json
import datetime
import os
import expense

class Tracker:
    

    def __init__(self):
        self.expenses = []


    def add_expense(self, expense: expense.Expense):
        if(os.path.exists('expenses.json')):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        
        if self.expenses:
            max_id = max(expense['id'] for expense in self.expenses)
            new_id = max_id + 1
        else:
            new_id = 1

        self.expenses.append({
            'id': new_id,
            'amount': expense.amount,
            'category': expense.category,
            'date': expense.date,
            'description': expense.description
        })
        
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)
        
        return self.expenses

    def update_expense(self, id: int, amount: float, category: str, description: str):
        if(os.path.exists('expenses.json')):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        for expense in self.expenses:
            if(expense["id"] == id):
                expense["amount"] = amount
                expense["category"] = category
                expense["description"] = description
                expense["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)
        
        return self.expenses
    
    def delete_expense(self, id: int):
        if(os.path.exists('expenses.json')):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        for expense in self.expenses:
            if(expense["id"] == id):
                self.expenses.remove(expense)

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)
        
        return self.expenses

    def show_summary(self):
        summary = 0

        if(os.path.exists('expenses.json')):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        for expense in self.expenses:
            summary += expense["amount"]

        print(f"\nSummary of the expenses: ${summary}")

    def show_expense(self):
        if(os.path.exists('expenses.json')):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        for expense in self.expenses:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Description: {expense['description']}")
    

