arr = [5, 2, 8, 1, 9, 3]

minimum = arr[0] + arr[1]
maximum = arr[0] + arr[1]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        total = arr[i] + arr[j]

        if total < minimum:
            minimum = total

        if total > maximum:
            maximum = total

print("Minimum Sum =", minimum)
print("Maximum Sum =", maximum)