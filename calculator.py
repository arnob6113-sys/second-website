num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("Choose operation: +  -  *  /")
op = input("Operation: ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")
