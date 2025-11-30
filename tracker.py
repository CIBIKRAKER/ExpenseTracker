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
        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")

            
        try:
            if self.expenses:
                max_id = max(expense['id'] for expense in self.expenses)
                new_id = max_id + 1
            else:
                new_id = 1
        except ValueError:
            new_id = 1

        try:    
            self.expenses.append({
                'id': new_id,
                'amount': expense.amount,
                'category': expense.category,
                'date': expense.date,
                'description': expense.description
            })
            
            with open('expenses.json', 'w') as file:
                json.dump(self.expenses, file, indent=4)
        except Exception as e:
            print(f"Error saving expense: {e}")

        console = Console()

        table = Table()

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="green")
        table.add_column("Description", style="magenta")
        table.add_column("Amount", justify="right", style="yellow")    
        table.add_column("Category", style="blue")

        for exp in self.expenses:
            date_short = exp['date'].split(" ")[0]  
            table.add_row(str(exp['id']), date_short, exp['description'], f"${exp['amount']}", exp['category'])

        console.print(table)
        
        return self.expenses

    def update_expense(self, id: int, amount: float, category: str, description: str):
        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")

        try:
            for expense in self.expenses:
                if(expense["id"] == id):
                    expense["amount"] = amount
                    expense["category"] = category
                    expense["description"] = description
                    expense["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("expenses.json", "w") as file:
                json.dump(self.expenses, file, indent=4)
        except Exception as e:
            print(f"Error updating expense: {e}")

        console = Console()

        table = Table()

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="green")
        table.add_column("Description", style="magenta")
        table.add_column("Amount", justify="right", style="yellow")
        table.add_column("Category", style="blue")

        for exp in self.expenses:
            date_short = exp['date'].split(" ")[0]  
            table.add_row(str(exp['id']), date_short, exp['description'], f"${exp['amount']}", exp['category'])

        console.print(table)

        return self.expenses
    
    def delete_expense(self, id: int):
        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")
        
        
        try:
            for expense in self.expenses:
                if(expense["id"] == id):
                    self.expenses.remove(expense)

            with open("expenses.json", "w") as file:
                json.dump(self.expenses, file, indent=4)
        except Exception as e:
            print(f"Error deleting expense: {e}")

        console = Console()

        table = Table()

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="green")
        table.add_column("Description", style="magenta")
        table.add_column("Amount", justify="right", style="yellow")
        table.add_column("Category", style="blue")

        for exp in self.expenses:
            date_short = exp['date'].split(" ")[0]  
            table.add_row(str(exp['id']), date_short, exp['description'], f"${exp['amount']}", exp['category'])

        console.print(table)

        return self.expenses

    def show_summary(self):
        summary = 0

        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")

        try:
            for expense in self.expenses:
                summary += expense["amount"]
            print(f"\nSummary of the expenses: ${summary}")
        except Exception as e:
            print(f"Error calculating summary: {e}")
            
        

    def show_summary_month(self, month: int, year: int):
        summary = 0
        
        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")
        
        try:
            for expense in self.expenses:
                exp_date = datetime.datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S")
                if exp_date.month == month and exp_date.year == year:
                    summary += expense["amount"]

            print(f"\nSummary of the expenses for {month}/{year}: ${summary}")
        except Exception as e:
            print(f"Error calculating monthly summary: {e}")


    def show_expenses(self):
        console = Console()

        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")

        table = Table()

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="green")
        table.add_column("Description", style="magenta")
        table.add_column("Amount", justify="right", style="yellow")    
        table.add_column("Category", style="blue")

        for exp in self.expenses:
            date_short = exp['date'].split(" ")[0]  
            table.add_row(str(exp['id']), date_short, exp['description'], f"${exp['amount']}", exp['category'])

        console.print(table)

    def to_csv(self):
        try:
            if(os.path.exists('expenses.json')):
                with open('expenses.json', 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except Exception as e:
            print(f"Error loading expenses: {e}")


        with open('expenses.csv', 'w') as file:
            file.write("ID,Date,Description,Amount,Category\n")
            for exp in self.expenses:
                file.write(f"{exp['id']},{exp['date']},{exp['description']},{exp['amount']},{exp['category']}\n")