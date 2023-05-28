"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""


# This function adds two numbers
def add(x, y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


def divide(x, y):
    """
    Short description.

    Long description

    Args:
        x (int): This is the first param.
        y (int): This is a second param.

    Returns:
        int: This is a description of what is returned.

    Raises:
        None in this case, can leave this part out if none."""
    return x / y


def main():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # check if choice is one of the four options
        if choice in {"1", "2", "3", "4"}:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == "1":
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == "2":
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == "3":
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == "4":
                print(num1, "/", num2, "=", divide(num1, num2))

            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
