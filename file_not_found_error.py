try:
    file = open("student.txt", "r")

    data = file.read()
    print(data)

    file.close()

except FileNotFoundError:
    print("Error: File not found")