import expense
import tracker
import argparse


def main():

    expense_tracker = tracker.Tracker()

    parser = argparse.ArgumentParser(description="ExpenseTracker")

    subparsers = parser.add_subparsers(dest="command")

    #Add expense
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description",type=str, required=True)
    add_parser.add_argument("--amount",type=float, required=True)
    add_parser.add_argument("--category",type=str, required=True)

    #Update expense
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id",type=int)
    update_parser.add_argument("--description",type=str, required=True)
    update_parser.add_argument("--amount",type=float, required=True)
    update_parser.add_argument("--category",type=str, required=True)

    #Delete expense
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id",type=int, required=True)

    #List
    list_parser = subparsers.add_parser("list")

    #Summary
    summary_parser = subparsers.add_parser("summary")

    #Summary by month
    summary_month_parser = subparsers.add_parser("summary_month")
    summary_month_parser.add_argument("--month",type=int, required=True)
    summary_month_parser.add_argument("--year",type=int, required=True)

    

    #CSV export
    csv_parser = subparsers.add_parser("to_csv")
    
    args = parser.parse_args()

    if args.command == "add":
        try:
            new_expense = expense.Expense(args.description, args.amount, args.category)
            expense_tracker.add_expense(new_expense)
        except Exception as e:
            print(f"Error adding expense: {e}")

    elif args.command == "update":
        try:
            expense_tracker.update_expense(args.id, args.amount, args.category, args.description)
        except Exception as e:
            print(f"Error updating expense: {e}")

    elif args.command == "delete":
        try:
            expense_tracker.delete_expense(args.id)
        except Exception as e:
            print(f"Error deleting expense: {e}")

    elif args.command == "list":
        try:
            expense_tracker.show_expenses()
        except Exception as e:
            print(f"Error listing expenses: {e}")

    elif args.command == "summary":
        try: 
            expense_tracker.show_summary()
        except Exception as e:
            print(f"Error showing summary: {e}")
            
    elif args.command == "summary_month":
        try:
            expense_tracker.show_summary_month(args.month, args.year)
        except Exception as e:
            print(f"Error showing monthly summary: {e}")
    elif args.command == "to_csv":
        try:
            expense_tracker.to_csv()
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

        
    

if __name__ == "__main__":
    main()