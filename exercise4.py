a = int(input("Please add number of line you want to print : "))
b = bool(int(input("Enter 1 for true and 0 for false : ")))


def star(a, b):
    if b:
        c = 1

        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a, b)
