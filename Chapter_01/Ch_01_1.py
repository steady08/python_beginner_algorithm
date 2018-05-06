import time


# Minus methods
def get_gcd(u, v):
    while u != 0:
        if u < v:
            t = u
            u = v
            v = t
        u = u - v
    return v


# Modulus methods
def gcd_modulus(u, v):
    while v != 0:
        t = u % v
        u = v
        v = t
    return u


# Recursion methods
def gcd_recursion(u, v):
    if v == 0:
        return u
    else:
        return gcd_recursion(v, u % v)


# Main function
LOOP = 10000

print("Input 0 to end program")

while True:
    print()
    first_input = int(input("Input first integer : "))
    second_input = int(input("Input second integer : "))

    if first_input < 0 or second_input < 0:
        print("Please input positive integer")

    if first_input == 0 or second_input == 0:
        print("End of program")
        break

    start_time = time.process_time()
    for i in range(0, LOOP):
        gcd = get_gcd(first_input, second_input)
    end_time = time.process_time()
    print("Minus methods : GCD of", first_input, "and", second_input, "is", gcd, "in", end_time-start_time)

    start_time = time.process_time()
    for i in range(0, LOOP):
        gcd = gcd_modulus(first_input, second_input)
    end_time = time.process_time()
    print("Modulus methods : GCD of", first_input, "and", second_input, "is", gcd, "in", end_time-start_time)

    start_time = time.process_time()
    for i in range(0, LOOP):
        gcd = gcd_recursion(first_input, second_input)
    end_time = time.process_time()
    print("Recursion methods : GCD of", first_input, "and", second_input, "is", gcd, "in", end_time-start_time)
