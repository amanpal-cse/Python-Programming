s = input("Enter a string: ")
count = 0

for ch in s:
    if ch.isdigit():
        count += 1

print("Digits =", count)