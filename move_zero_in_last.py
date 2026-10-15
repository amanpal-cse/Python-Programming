list = [0, 1, 0, 3, 12]
for i in list:
    if i == 0:
        list.remove(i)
        list.append(0)
print(list)