# File: long_python_code.py

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    """Print all prime numbers up to a given limit."""
    if limit < 2:
        print("There are no prime numbers in the specified range.")
    else:
        print("Prime numbers up to", limit, "are:")
        for num in range(2, limit + 1):
            if is_prime(num):
                print(num, end=" ")

if __name__ == "__main__":
    print("This is a Python script with some functions.")
    print("The 10th Fibonacci number is:", fibonacci(10))
    
    user_input = int(input("Enter a number to check if it's prime: "))
    if is_prime(user_input):
        print(user_input, "is a prime number.")
    else:
        print(user_input, "is not a prime number.")

    limit_input = int(input("Enter a limit to print prime numbers up to: "))
    print_primes_up_to(limit_input)
