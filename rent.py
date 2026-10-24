print("\n --- RENT CALCULATOR ---")

expense_name = ""
expense_price = 0
total = 0
expenses = []
tenants = 0

while tenants <= 0:
    tenants = int(input("Enter the number of tenants: "))

while expense_name != "quit":
    expense_name = input("Enter the name of the expense or 'Quit' to stop: ").lower()
    while expense_name == "":
        print("Expense name cannot be empty")
        expense_name = input("Enter the name of the expense: ")
        
    if expense_name != "quit":
        expense_price = float(input("Enter the price of the expense: "))
        while expense_price <= 0:
            print("Expense price cannot be less than 0")
            expense_price = float(input("Enter the price of the expense: "))
    
        expenses += [[expense_name, expense_price]]
        
        total += expense_price
        
        print(f"Expense: {expense_name} \nAmount: {expense_price}XAF ")
    
amt_per_tenant = total / tenants

print("\n--- EXPENSES ---")

for expense in expenses:
    print(f"Expense name: {expense[0]}")
    print(f"Amount: {expense[1]}  XAF \n")

print(f"Number of tenants: {tenants} tenants")
print(f"Amount per tenant: {amt_per_tenant} XAF")
print(f"Total amount: {total} XAF")