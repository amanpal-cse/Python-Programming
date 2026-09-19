employees = []


def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("Employee added successfully!")


def display_employees():
    if not employees:
        print("No employees found.")
        return

    print("\n===== EMPLOYEE LIST =====")

    for emp in employees:
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Department:", emp["department"])
        print("Salary:", emp["salary"])
        print("------------------------")


def search_employee():
    emp_id = input("Enter employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found!")
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Department:", emp["department"])
            print("Salary:", emp["salary"])
            return

    print("Employee not found.")


def delete_employee():
    emp_id = input("Enter employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found.")


while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice!")