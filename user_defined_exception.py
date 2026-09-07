class InvalidAgeError(Exception):
    pass


age = int(input("Enter your age: "))

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("You are eligible.")

except InvalidAgeError as e:
    print("Error:", e)