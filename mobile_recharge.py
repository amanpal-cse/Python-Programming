balance = 100
try:
    recharge = float(input("Enter recharge amount : "))

    if recharge <= 0:
        raise ValueError("Recharge amount must be positive")

    balance = balance + recharge
    print("Recharge Successfully")
    print("New balance :",balance)
except ValueError as error:
    print("recharge failed:",error)