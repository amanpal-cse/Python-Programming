while True:
    name = input("enter customer's name: ")
    total = 0
    
    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        
        total += amount * quantity
        
        repeat = input("do you want to add more items? (yes/no): ")
        if repeat.lower() == "no":
            break  
            
    print("-"* 40)
    print("Name : ",name)
    print("Amount to be paid : ",total)
    print("-" * 40)
    print("===== Happy Shopping =====")
    next_customer = input("Is there another customer? (yes/no): ")
    if next_customer.lower() == "no":
        break  