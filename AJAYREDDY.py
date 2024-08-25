import json
from datetime import datetime

DATA_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from a JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense."""
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        category = input("Enter category: ")
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_summary(expenses, month):
    """View a summary of expenses for a given month."""
    total = 0
    catego
