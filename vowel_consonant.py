ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an Alphabet")