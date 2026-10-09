students = []

def input_marks():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    print("\nEnter marks out of 100:")
    english = float(input("English: "))
    maths = float(input("Maths: "))
    science = float(input("Science: "))
    python_marks = float(input("Python: "))
    java = float(input("Java: "))

    total = english + maths + science + python_marks + java
    percentage = total / 5
    if (english < 35 or maths < 35 or science < 35
            or python_marks < 35 or java < 35):
        result = "Fail"
        grade = "F"
    else:
        result = "Pass"
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 45:
            grade = "C"
        else:
            grade = "D"

    student = {
        "roll_no": roll_no,
        "name": name,
        "english": english,
        "maths": maths,
        "science": science,
        "python": python_marks,
        "java": java,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    students.append(student)
    print("\nMarks entered successfully!")
def display_result():
    if not students:
        print("\nNo student records found!")
        return
    for s in students:
        print("\n  STUDENT RESULT ")
        print("Roll Number:", s["roll_no"])
        print("Student Name:", s["name"])
        print("English Marks:", s["english"])
        print("Maths Marks:", s["maths"])
        print("Science Marks:", s["science"])
        print("Python Marks:", s["python"])
        print("Java Marks:", s["java"])
        print("Total Marks:", s["total"], "/ 500")
        print("Percentage:", round(s["percentage"], 2), "%")
        print("Grade:", s["grade"])
        print("Result:", s["result"])

while True:
    print("\n1. Input Student Marks")
    print("2. Display Student Result")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks()
    elif choice == "2":
        display_result()
    elif choice == "3":
        print("Program Ended.")
        break
    else:
        print("Invalid choice! Try again.")