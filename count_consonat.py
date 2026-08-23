s = input("Enter a string: ")
count = 0

for ch in s:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Consonants =", count)