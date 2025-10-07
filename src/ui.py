import storage
from datetime import datetime
"Function to add expense into the csv file"

def add_expense():
  data = {}

  filename = storage.choose_expense_file()

  amount = storage.parse_amount(input("Amount: ")) 
  date = input("Date [YYYY-MM-DD] (Leave Empty for Today's Date ): ")  
  category = input("Please input category for this expense:")
  note = input("Add notes? :  ")
  
  if (date):
    storage.parse_date(date)
    data["Date"] = date 
  else:
    data["date"] =  datetime.date(datetime.now())  
    data["amount"] = amount
    data["category"] = category
    data["note"] = note


  if (data): 
   storage.save_expense(data,filename)
  else:
    pass
  

def view_expenses():
    filename = storage.choose_expense_file()
    expenses = storage.get_expenses(filename)
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nYour Expenses:")
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']} - ₦{exp['amount']} - {exp['note']}")


