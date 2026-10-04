print("Simple Calculator")

first_number = float(input("Enter the first number: "))
operator = input("Choose an operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("You cannot divide by zero.")
    else:
        result = first_number / second_number
        print("Result:", result)
else:
    print("That operation is not supported.")

if operator in ["+", "-", "*"]:
    print("Result:", result)