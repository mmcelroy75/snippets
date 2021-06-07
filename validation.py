def yes_no_validation(prompt):  # A simple yes/no validation function

    answer = input(prompt).strip().upper()

    if answer[:1] not in ['Y', 'N']:
        print("Your answer must be 'Y' or 'N'.")
        return yes_no_validation(prompt)

    if answer == 'Y':
        return True
    else:
        return False


def input_validation(prompt, a, b):  # Function to validate choice in range between a and b
    while True:
        try:
            x = int(input(prompt))
            if (x < a or x > b):
                raise ValueError
            break

        except ValueError:
            print(f"That is not a valid choice. Please enter {a} through {b}.")

    return x


def int_validation(prompt, x):  # Function to validate integer input
    while True:
        try:
            num = int(input(prompt))
            if (not isinstance(num, int)) or (num < x):
                raise ValueError
            break

        except ValueError:
            print("You must enter a non-negative whole number.")

    return num


def float_validation(prompt, x):  # Function to validate float input
    while True:
        try:
            num = int(input(prompt))
            if (not isinstance(num, float)) or (num < x):
                raise ValueError
            break

        except ValueError:
            print("You must enter a non-negative whole number.")

    return num
