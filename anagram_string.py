s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")