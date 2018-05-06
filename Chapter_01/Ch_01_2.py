import time
import math


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime2(n):
    sqrn = int(math.sqrt(n))
    for i in range(2, sqrn+1):
        if n % i == 0:
            return False
    return True


def print_results(i, n, r, t):
    if r:
        print('Test case', i, ":", n, "is prime in", t)
    else:
        print('Test case', i, ":", n, "is not prime in", t)


# Main function
LOOP = 10000

print("Test input number is prime or not")
print("Input 0 to end program")

while True:
    print()
    input_data = int(input("Input number to test -> "))

    if input_data < 0:
        print("Please input positive integer")

    if input_data == 0:
        print("End of program")
        break

    start_time = time.process_time()
    for i in range(0, LOOP):
        test_result = is_prime(input_data)
    end_time = time.process_time()
    print_results(1, input_data, test_result, end_time-start_time)

    start_time = time.process_time()
    for i in range(0, LOOP):
        test_result = is_prime2(input_data)
    end_time = time.process_time()
    print_results(2, input_data, test_result, end_time-start_time)
