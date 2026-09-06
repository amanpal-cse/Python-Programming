try:
    num = int(input("Enter a number: "))
    print("Number =", num)

except ValueError:
    print("Error: Please enter a valid number")