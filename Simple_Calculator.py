# Simple calculator

def format_number(value):
    """
    Display whole numbers without .0,
    but keep decimals when needed.
    """
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def calculator():
    """Run a simple calculator program."""
    
    print("Simple Python Calculator")
    print("------------------------")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please run the program again.")
        return
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return
    
    if choice == "1":
        result = add(num1, num2)
        print(f"{format_number(num1)} + {format_number(num2)} = {format_number(result)}")
        
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"{format_number(num1)} - {format_number(num2)} = {format_number(result)}")
        
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"{format_number(num1)} * {format_number(num2)} = {format_number(result)}")
        
    elif choice == "4":
        result = divide(num1, num2)
        
        if isinstance(result, str):
            print(result)
        else:
            print(f"{format_number(num1)} / {format_number(num2)} = {format_number(result)}")
            
calculator()
