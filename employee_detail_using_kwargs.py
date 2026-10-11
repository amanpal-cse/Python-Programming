def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

employee_details(name="Aman",age=25, salary=100000,department="CSE")