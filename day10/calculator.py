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

num1 = float(input("What's the first number?: "))

simbols = []


def show_operation():
    for operation in operations:
        simbols.append(operation)
        print(operation)


show_operation()
operation_simb = input("pick an operation from the line above: ")
if operation_simb not in simbols:
    print("invalid")
else:
    num2 = float(input("what's the second number?: "))

    def get_result(nu1, nu2):
        for simbol in operations:
            if operation_simb == simbol:
                answe = operations[simbol](nu1, nu2)
                return answe

    first_result = get_result(num1, num2)
    result_final = first_result
    add_more = True
    while add_more:
        ask = input(
            "Do you want to do more calculations? 'yes' or 'no': ").lower()
        possibilities = ('yes', 'no')
        if ask not in possibilities:
            print("invalid choice")
        else:
            if ask == "yes":
                show_operation()
                operation_simb = input(
                    "pick an operation from the line above: ")
                if operation_simb not in simbols:
                    add_more = False
                    print("We'll stop right here, the result until now is: {}".format(
                        result_final))
                else:
                    num3 = int(input("type the number: "))
                    new_result = (get_result(first_result, num3))
                    result_final = new_result
            elif ask == 'no':
                add_more = False
                print(f"the result is: {result_final}")
