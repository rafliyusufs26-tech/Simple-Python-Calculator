def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    # Validation when divide with zero
    if y == 0:
        return "Error: You can't divide zero!"
    return x / y

def calc():
    print("=== Simple Calculator ===")
    
    while True:
        print("\nPick the operation: ")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiply (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Pick the number (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                # Using a float to use int and decimal number
                num1 = float(input("Input the first number: "))
                num2 = float(input("Input the second number: "))
            except ValueError:
                print("Input is invalid. Please try again.")
                continue
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {mult(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {div(num1, num2)}")
        else:
            print("Your choice is invalid. Please try again.")

# Run the program
if __name__ == "__main__":
    calc()
