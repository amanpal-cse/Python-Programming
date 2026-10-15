s = input("Enter a string: ")

upper = 0
lower = 0
digit = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)