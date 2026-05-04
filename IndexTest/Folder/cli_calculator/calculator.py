import argparse
import sys

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts b from a."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides a by b. Raises ValueError on zero division."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    parser = argparse.ArgumentParser(description="A simple CLI Calculator.")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="The operation to perform.")
    parser.add_argument("num1", type=float, help="The first number.")
    parser.add_argument("num2", type=float, help="The second number.")

    args = parser.parse_args()

    try:
        if args.operation == "add":
            result = add(args.num1, args.num2)
        elif args.operation == "sub":
            result = subtract(args.num1, args.num2)
        elif args.operation == "mul":
            result = multiply(args.num1, args.num2)
        elif args.operation == "div":
            result = divide(args.num1, args.num2)
        
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
