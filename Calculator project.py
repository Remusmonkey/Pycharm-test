def addition(term_1, term_2):
    return term_1 + term_2
def subtraction(term_1, term_2):
    return term_1 - term_2
def multiply(term_1, term_2):
    return term_1 * term_2
def divide(term_1, term_2):
    if term_2 == 0:
        return "Cannot divide by 0.  Please use a non-zero number."
    else:
        return term_1 / term_2

while True:
    print('''Welcome to the calculator. Please select an operation.
    1. Add
    2. Subtract
    3. Divide
    4. Multiply
    5. Exit''')
    operation = int(input('Operation Number: '))


    if operation == 5:
        print("Exiting Calculator")
        break

    term_1 = float(input('First number:  '))
    term_2 = float(input('Second number:  '))

    if operation == 1:
        print(term_1, "+", term_2, "=", addition(term_1, term_2))

    elif operation == 2:
        print(term_1, "-", term_2, "=", subtraction(term_1, term_2))

    elif operation == 3:
        print(term_1, "/", term_2, "=", divide(term_1, term_2))

    elif operation == 4:
        print(term_1, "*", term_2, "=", multiply(term_1, term_2))

    else:
        print("Please choose a valid operation.")