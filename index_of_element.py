t = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

if element in t:
    print("Index:", t.index(element))
else:
    print("Element Not Found")