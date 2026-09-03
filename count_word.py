with open("demo.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total Words:", len(words))