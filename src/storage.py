# the csv read and write file
import os,csv

HEADER = ["Date","Amount","Category","Note"]
# Function for save expense to the csv and operations on the csv file 
#Check cant add expenses to the csv file
def save_expense(row,filename="data/expenses.csv"):
    os.makedirs(os.path.dirname(filename),exist_ok= True)
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f,HEADER)
        if not file_exists:
            writer.writeheader()
            writer.writerow(row)

         
from datetime import datetime
def parse_amount(s):
    try:
        return float(s)
    except ValueError:
        raise ValueError("Enter a valid number for amount")

def parse_date(s):
    # Accept common formats but store as ISO
    for fmt in ("%Y-%m-%d","%d/%m/%Y","%d-%m-%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError("Date must be like YYYY-MM-DD or DD/MM/YYYY")

# Usage in add_expense:

