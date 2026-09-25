str1 = input("Enter a string:")
n = int(input("Enter the index position of the character to be removed:"))
first_part  = str1[ :n-1]
last_part = str1[n: ]
print("The new string after removing the charachter = ",(first_part + last_part))