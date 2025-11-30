# Expense Tracker (CLI)

A simple command-line Expense Tracker written in Python.  
It allows you to add, update, delete, list, summarize, and export expenses to CSV.  
All data is stored locally in expenses.json and displayed using Rich tables.

## 🚀 Features

- ➕ Add new expenses  
- ✏️ Update existing expenses  
- ❌ Delete expenses by ID  
- 📋 List all expenses in a formatted table  
- 📊 Show total summary  
- 🗓️ Show monthly summary (by month & year)  
- 📤 Export all expenses to CSV (`expenses.csv`)  
- 🆔 Automatically incrementing expense IDs  
- 💾 Persistent JSON storage  

## 📦 Requirements

- Python 3.10+
- Install dependencies:
  ```bash
  pip install rich
  pip install argparse


## Usage and Commands:

Run any command like:

    python app.py <command> [options]

## Commands:
Add an expense:

    python app.py add --description "Coffee" --amount 3.50 --category food

Update an expense:

    python app.py update --id 2 --description "Lunch" --amount 12.90 --category food

Delete an expense:

    python app.py delete --id 3

List all expenses:

    python app.py list

Show total summary:

    python app.py summary

Show monthly summary:

    python app.py summary_month --month 11 --year 2025

Export all expenses to CSV:

    python app.py to_csv
