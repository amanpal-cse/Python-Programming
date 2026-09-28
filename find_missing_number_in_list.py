def find_missing(a):
    n = len(a) + 1

    total = n * (n + 1) // 2

    sum_list = sum(a)

    return total - sum_list


a = [1, 2, 3, 5, 6]

print("Missing number:", find_missing(a))