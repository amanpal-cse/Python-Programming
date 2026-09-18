# Student Management System

students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully.")

    # Display Students
    elif choice == 2:

        if len(students) == 0:
            print("No student records found.")

        else:
            print("\n--- Student Records ---")

            for student in students:
                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                print("----------------------")

    # Search Student
    elif choice == 3:
        roll = int(input("Enter Roll Number to search: "))

        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == 4:
        roll = int(input("Enter Roll Number to delete: "))

        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully.")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")