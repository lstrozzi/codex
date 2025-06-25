# Simple Python Program Example

def greet_by_name(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_by_name(user_name)
    print("\nLet's do some math!")
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
