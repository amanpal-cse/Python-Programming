str1 = input("Enter a string : ")
if len(str1) < 2:
    print(None)
else:
    print("String made from last two character of both ends:",str1[0:2] + str1[-2 : ])