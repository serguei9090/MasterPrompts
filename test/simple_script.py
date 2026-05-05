import random

def get_random_number():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)

def print_hello(name):
    """Accepts an argument and prints 'hello {name}'."""
    print(f"hello {name}")

def add(a, b):
    """Accepts two arguments and returns their sum."""
    return a + b

def multiply(a, b):
    """Accepts two arguments and returns their product."""
    return a * b

def square(n):
    """Accepts one argument and returns its square."""
    return n * n

if __name__ == "__main__":
    # Demonstration of the functions
    num = get_random_number()
    print(f"Random number: {num}")
    
    print_hello("World")
    
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"12 squared = {square(12)}")
