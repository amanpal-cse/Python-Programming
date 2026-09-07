try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input!")

finally:
    print("Program execution completed.")