import json
import datetime
import os
import expense
from rich.console import Console
from rich.table import Table

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

    def show_expenses(self):
        console = Console()

        if(os.path.exists('expenses.json')):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        table = Table()

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="green")
        table.add_column("Description", style="magenta")
        table.add_column("Amount", justify="right", style="yellow")    

        for exp in self.expenses:
            date_short = exp['date'].split(" ")[0]  
            table.add_row(str(exp['id']), date_short, exp['description'], f"${exp['amount']}")

        console.print(table)