books = []

def add_book():
    book = input("Enter book name: ")
    author = input("Enter author name: ")

    books.append({
        "book": book,
        "author": author,
        "issued": False
    })

    print("Book added successfully!")


def display_books():
    if not books:
        print("No books available.")
        return

    print("\n--- Book List ---")
    for i, b in enumerate(books, 1):
        status = "Issued" if b["issued"] else "Available"
        print(i, b["book"], "-", b["author"], "-", status)


def issue_book():
    book = input("Enter book name to issue: ")

    for b in books:
        if b["book"].lower() == book.lower():
            if not b["issued"]:
                b["issued"] = True
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book = input("Enter book name to return: ")

    for b in books:
        if b["book"].lower() == book.lower():
            if b["issued"]:
                b["issued"] = False
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return

    print("Book not found.")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")