from art import logo
print(logo)

# calculator
# add


def add(n1, n2):
    return n1 + n2
# subtraction


def sub(n1, n2):
    return n1 - n2
# multiplication


def mult(n1, n2):
    return n1 * n2
# division


def div(n1, n2):
    return n1 / n2


"""
simbols = ['+', '-', '*', '/']
# first number
num1 = int(input("type the first number: \n"))
# operantion
operator = input(
    "choose what operantion do you want to use '+', '-','/','*': \n")
if operator not in simbols:
    print("invalid choice")
# second number if operator is valid
else:
    num2 = int(input("type the second number"))

    if operator == "+":
        print(f"result: {add(num1, num2)}")
    elif operator == "-":
        print(f"result: {sub(num1, num2)}")
    elif operator == "/":
        print(f"result: {div(num1, num2)}")
    elif operator == "*":
        print(f"result: {mult(num1, num2)}")
"""

# mixing dictionaries and function
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

num1 = int(input("What's the first number?: "))
for operation in operations:
    print(operation)
operation_simb = input("pick an operation from the line above: ")
num2 = int(input("what's the second number?: "))
for simbol in operations:
    if operation_simb == simbol:
        answe = operations[simbol](num1, num2)


print(f"{num1} {operation_simb} {num2} = {answe}")
