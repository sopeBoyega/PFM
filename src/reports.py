import pandas as pd
import storage
from tabulate import tabulate
import datetime


# Load DataFrame which is a 2 diensional data type we work with in panda
def load_df():
 filename = storage.choose_expense_file()

 df = pd.read_csv(filename,parse_dates=["date"])
 df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
 df = df.dropna(subset=["date","amount"])
  

 return df 
# The function below gets the total spending of each month 
def totals_per_month(df):
    # create Year-Month column
    df["month"] = df["date"].dt.to_period("M")
    monthly = df.groupby("month")["amount"].sum().sort_index()
    # convert PeriodIndex to strings if printing
    return monthly

# This function groups the total per categories
def totals_per_category(df):
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)

def generate_reports():
  df = load_df()
  monthly =  totals_per_month(df)
  monthly_table = [[idx, val] for idx, val in monthly.items()]
#   Using the tabulate module I installed to print out a proper format in my CLI
  print(tabulate(monthly_table,headers=["Month","Total"],tablefmt="grid"))
  categories = totals_per_category(df)

  categories_table = [[idx , val] for idx ,val in categories.items()]
  print(tabulate(categories_table,headers=["Category","Total"],tablefmt="grid"))




