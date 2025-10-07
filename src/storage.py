import os, csv
from datetime import datetime

# Consistent headers (lowercase)
HEADER = ["date", "amount", "category", "note"]

# Base paths
BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
EXPENSES_DIR = os.path.join(BASE_DIR, "expenses")
os.makedirs(EXPENSES_DIR, exist_ok=True)


# List available CSV files
def list_expense_files():
    return [f for f in os.listdir(EXPENSES_DIR) if f.endswith(".csv")]


# Save a row to a CSV file
def save_expense(row, filename=None):
    if not filename:
        filename = os.path.join(EXPENSES_DIR, "expenses.csv")

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


# Let user choose a file or create a new one
def choose_expense_file():
    files = list_expense_files()
    if not files:
        print("No expense files found. Let's create a new one.")
        name = input("Enter new file name (without .csv): ").strip()
        return os.path.join(EXPENSES_DIR, f"{name}.csv")
    

    # Correct the code so that you can only add expenses when youre just want to add an expennse 
    print("\nChoose a file to add expenses to,view expenses or generate reports for:")
    for i, f in enumerate(files, start=1):
        print(f"{i}) {f}")
    print(f"{len(files)+1}) [Create new file]")

    choice = input("> ").strip()
    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(files):
            return os.path.join(EXPENSES_DIR, files[idx-1])
        elif idx == len(files)+1:
            name = input("Enter new file name (without .csv): ").strip()
            return os.path.join(EXPENSES_DIR, f"{name}.csv")

    # fallback
    return os.path.join(EXPENSES_DIR, "default.csv")


# Read all expenses from a CSV
def get_expenses(filename):
    expenses = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)   # each row is already a dict
    except FileNotFoundError:
        print("No expenses found yet.")
    return expenses


# Validation helpers
def parse_amount(s):
    try:
        return float(s)
    except ValueError:
        raise ValueError("Enter a valid number for amount")


def parse_date(s):
    if not s.strip():  # empty → default today
        return datetime.now().date().isoformat()

    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError("Date must be like YYYY-MM-DD or DD/MM/YYYY")
