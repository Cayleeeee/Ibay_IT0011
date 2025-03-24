def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if a > b:
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("Select an operation:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == "Q":
            break
        
        if choice in ["D", "E", "R", "F"]:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                
                if choice == "D":
                    result = divide(num1, num2)
                elif choice == "E":
                    result = exponentiate(num1, num2)
                elif choice == "R":
                    result = remainder(num1, num2)
                elif choice == "F":
                    result = summation(num1, num2)
                
                if result is None:
                    print("Invalid input, please try again.")
                else:
                    print("Result:", result)
            except ValueError:
                print("Please enter valid numbers.")
        else:
            print("Invalid choice, please try again.")

main()
