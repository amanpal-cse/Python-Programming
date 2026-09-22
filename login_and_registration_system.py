users = {}

while True:
    print("\n--- Login & Registration System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Registration
    if choice == "1":
        username = input("Enter username: ")

        if username in users:
            print("Username already exists!")
        else:
            password = input("Enter password: ")

            users[username] = password

            print("Registration successful!")

    # Login
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            print("Welcome", username)
        else:
            print("Invalid username or password!")

    # Exit
    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")