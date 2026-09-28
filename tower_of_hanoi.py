def move(src, dst):
    print("Move disk from", src, "to", dst)


def hanoi(n, src, dst, aux):
    if n == 0:
        return

    hanoi(n - 1, src, aux, dst)

    move(src, dst)

    hanoi(n - 1, aux, dst, src)

n = int(input("Enter number of disks: "))

hanoi(n, "A", "C", "B")