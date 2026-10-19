def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1/num2

def multiply(num1, num2):
    return num1*num2

def calculation():
    """Defines a calculation. The result of the previous calculation will be used in the next iteration."""

    try:
        num1 = int(input("Enter your first number: "))
    except Exception as e:
        print(f"You didn't enter a number. {e}")
        raise e

    go_on = True

    while (go_on):
        operation = input("What operation would you like to use? (+ - * /): ")

        try:
            num2 = int(input("Enter your second number: "))
        except Exception as e:
            print(f"Enter a valid number. {e}")
            raise e

        result = 0

        match operation:
            case "+":
                result = add(num1, num2)
            case "-":
                result = substract(num1, num2)
            case "*":
                result = multiply(num1, num2)
            case "/":
                result = divide(num1, num2)
            case _:
                print("Invalid operation, ignoring this calculation.")

        print(f'Result: {result}')
        go_on = input("Would you like to continue? (yes/no): ") == "yes"
        num1 = result


def main():
    go_on = True
    while(go_on):
        calculation()

        go_on = input("New Operation? (yes/no): ") == "yes"

main()
