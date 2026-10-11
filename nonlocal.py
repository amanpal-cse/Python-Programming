def num1():
    a = 10

    def num2():
        nonlocal a
        a = 20

    num2()
    print("Value is a:", a)
num1()