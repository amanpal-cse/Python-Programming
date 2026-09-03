with open("demo.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")