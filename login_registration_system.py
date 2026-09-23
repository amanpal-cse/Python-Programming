users = {}

def register():
    username = input("Enter username: ")

    if username in users:
        print("Username already exists!\n")
        return
    
    password = input("Enter password: ")
    users[username] = password
    print("Registration successful!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        print("Welcome", username)
    else:
        print("Invalid username or password!")
    print()
while True:
    print("===== LOGIN & REGISTRATION SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!\n")