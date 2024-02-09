print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("")

while True:
    try:
        choice = int(input("Please select from 1/2/3/4: "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 1:
        try:
            num1 = float(input("Please select a number: "))
            num2 = float(input("Please select a second Number: "))
        except ValueError:
            print("---------------------------------------------")
            print("")
            print("1. Addition")
            print("2. Subtraction")
            print("3. multiplication")
            print("4. Division")
            print("")
            print("invalid number detected please try again.")
            continue
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
            exit_program = input("Do you want to exit the program (Y/N): ")
            modified_exit = exit_program.lower()
            if modified_exit == "y":
                break
            else:
                print("---------------------------------------------")
                print("")
                print("1. Addition")
                print("2. Subtraction")
                print("3. multiplication")
                print("4. Division")
                print("")
                continue
    if choice == 2:
        try:
            num1 = float(input("Please select a number: "))
            num2 = float(input("Please select a second Number: "))
        except ValueError:
            print("---------------------------------------------")
            print("")
            print("1. Addition")
            print("2. Subtraction")
            print("3. multiplication")
            print("4. Division")
            print("")
            print("Invalid input detected. Please try again.")
            continue
        else:
            print(f"{num1} - {num2} = {num1 - num2}")
            exit_program = input("Do you want to exit the program (Y/N): ")
            modified_exit = exit_program.lower()
            if modified_exit == "y":
                break
            else:
                print("---------------------------------------------")
                print("")
                print("1. Addition")
                print("2. Subtraction")
                print("3. multiplication")
                print("4. Division")
                print("")
                continue
    if choice == 3:
        try:
            num1 = float(input("Please select a number: "))
            num2 = float(input("Please select a second Number: "))
        except ValueError:
            print("---------------------------------------------")
            print("")
            print("1. Addition")
            print("2. Subtraction")
            print("3. multiplication")
            print("4. Division")
            print("")
            print("Invalid input detected. Please try again.")
            continue
        else:
            print(f"{num1} * {num2} = {num1 * num2}")
            exit_program = input("Do you want to exit the program (Y/N): ")
            modified_exit = exit_program.lower()
            if modified_exit == "y":
                break
            else:
                print("---------------------------------------------")
                print("")
                print("1. Addition")
                print("2. Subtraction")
                print("3. multiplication")
                print("4. Division")
                print("")
                continue
    if choice == 4:
        try:
            num1 = float(input("Please select a number: "))
            num2 = float(input("Please select a second Number: "))
        except ValueError:
            print("---------------------------------------------")
            print("")
            print("1. Addition")
            print("2. Subtraction")
            print("3. multiplication")
            print("4. Division")
            print("")
            print("You invalid input detected. Please try again.")
            continue
        else:
            try:
                print(f"{num1} : {num2} = {num1 / num2}")
            except ZeroDivisionError:
                print(f" {num1} : {num2} = Infinity")
            exit_program = input("Do you want to exit the program (Y/N): ")
            modified_exit = exit_program.lower()
            if modified_exit == "y":
                break
            else:
                print("---------------------------------------------")
                print("")
                print("1. Addition")
                print("2. Subtraction")
                print("3. multiplication")
                print("4. Division")
                print("")
                continue
    if choice >= 5 or choice <= 0:
        print("Looks like you typed an invalid number.")