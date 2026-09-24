import tkinter as tk
from tkinter import messagebox

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or marks == "":
        messagebox.showwarning("Warning", "All fields are required")
        return

    students.append([roll, name, marks])

    student_list.insert(
        tk.END,
        f"Roll: {roll} | Name: {name} | Marks: {marks}"
    )

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Student Management")
window.geometry("500x500")

tk.Label(window, text="Student Management System",
         font=("Arial", 18)).pack(pady=20)

tk.Label(window, text="Roll Number").pack()
roll_entry = tk.Entry(window)
roll_entry.pack()

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Marks").pack()
marks_entry = tk.Entry(window)
marks_entry.pack()

tk.Button(window, text="Add Student",
          command=add_student).pack(pady=15)

student_list = tk.Listbox(window, width=60)
student_list.pack(pady=10)

window.mainloop()