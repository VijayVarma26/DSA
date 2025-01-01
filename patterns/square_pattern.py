# Print Square pattern like 
# 1 2 3
# 1 2 3
# 1 2 3


def print_square_pattern_star(n):
    for i in range(0,n):
        for j in range(1,n+1):
            print("*", end= " ")
        print()

def print_square_pattern_num(n):
    for i in range(0,n):
        for j in range(1,n+1):
            print(j, end= " ")
        print()


def print_square_pattern_char(n):
    for i in range(0,n):
        char = "A"
        for j in range(1,n+1):
            print(char, end= " ")
            # character cannot be incremented directly need to use chr() and ord()
            char = chr(ord(char) + 1) 
        print()

def print_square_pattern_inc_num(n):
    num =1
    for i in range(0,n):
        for j in range(1,n+1):
            print(num, end= " ")
            # character cannot be incremented directly need to use chr() and ord()
            num = num + 1 
        print()

print("Star Pattern")
print_square_pattern_star(5)


print("Num Pattern")
print_square_pattern_num(5)

print("Character Pattern")
print_square_pattern_char(5)

print("Num Pattern with num increasing")
print_square_pattern_inc_num(5)