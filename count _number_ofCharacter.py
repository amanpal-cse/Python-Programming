dict = {}
str1 = input("Enter a string:")
for n in str1:
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
print("Character frequency")
for k,v in dict.items():
    print(k,v)
