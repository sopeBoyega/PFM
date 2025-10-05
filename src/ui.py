import storage

"Function to add expense into the csv file"
def add_expense():
  data = {}
  amount = storage.parse_amount(input("Amount: "))
  date = storage.parse_date(input("Date [YYYY-MM-DD]: ")) 
  category = input("Please input category for this expense:")
  note = input("Add notes?")
  
  data["Date"] = date
  data["Amount"] = amount
  data["Category"] = category
  data["Note"] = note

  

  if (data): 
   storage.save_expense(data)
  else:
    pass
  
  

