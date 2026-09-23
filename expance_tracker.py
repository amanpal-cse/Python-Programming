expenses = []
def add_expense():
    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.\n")
        return
    print("\n----- Expense List -----")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Date: {expense['date']}")
        print(f"   Category: {expense['category']}")
        print(f"   Amount: ₹{expense['amount']}")
        print(f"   Note: {expense['note']}")
        print()

def total_expense():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total Expense = ₹{total}\n")
while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!\n")