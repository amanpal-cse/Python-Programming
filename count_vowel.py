str1 = input("Enter a string: ")
count = 0

for ch in str1:
    if ch in "aeiouAEIOU":
        count += 1

print("Total Vowels =", count)