numbers = [10, 20, 10, 30, 20, 40]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List after removing duplicates:", unique)