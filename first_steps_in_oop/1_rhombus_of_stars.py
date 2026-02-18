def print_row(size, stars):
    print(" " * (size - stars) + "* " * stars)

def print_up(size):
    for row in range(1, size):
        print_row(size, row)

def print_down(size):
    for row in range(size, 0, -1):
        print_row(size, row)

def print_rhombus(size):
    print_up(size)
    print_down(size)

n = int(input())

print_rhombus(n)