import ui
# The entry point of the finance system
def main_menu():
    while True:
        print("\n Expense Tracker")
        print("1.) Add Expenses")
        print("2.) View Expenses")
        print("3.) Generate Reports")
        print("q) Quit")
        choice = input(">").strip().lower()
        if choice == "1":
            ui.add_expense()
        elif choice == "2":
            # Implement function to view expenses
            view_expenses()    
        elif choice == "3":
            generate_report()    
        elif choice in ('q',"quit","exit"):
            break
        else:
            print("Unknown Option")



main_menu()             

