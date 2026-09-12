class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


s = Student("Aman", 85)

s.display()

s.set_marks(90)

s.display()