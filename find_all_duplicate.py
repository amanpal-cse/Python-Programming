def find_all_duplicates(a):
    i = 0
    n = len(a)
    dupes = []

    while i < n:
        c = a[i] - 1

        if a[i] != a[c]:
            a[i], a[c] = a[c], a[i]
        else:
            i += 1

    for i in range(n):
        if a[i] != i + 1:
            dupes.append(a[i])

    return dupes


a = [4, 3, 2, 7, 8, 2, 3, 1]

print("Duplicates:", find_all_duplicates(a))