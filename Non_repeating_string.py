str = input("Enter a string: ")

for s in str:
    if str.count(s) == 1:
        print(s)
        break
else:
    print("No non repeating character")