def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


def addition(first_num, second_num):
    result = first_num + second_num
    return result


def subtraction(first_num, second_num):
    result = first_num - second_num
    return result


def multiplication(first_num, second_num):
    result = first_num * second_num
    return result


def division(first_num, second_num):
    result = first_num / second_num
    return result


while True:
    start_option = input(
        "Press any key to start or exit to leave the progam"
    )
    if start_option.lower() == 'exit':
        break
    

print("Option A to addition or substrac")
print("Option B to multiply or divide")
print("Option C to get root square")
print("Option D to raise to power")


option = input("Choose an option")


if option.lower() == 'a':
    try:
        print("Option A to addition")
        print("Option B to subtraction")


        operation = input("Choose an option: ")


        if operation.lower() == 'a':


            try:
                print(
                    addition(
                        float(input("First number: ")),
                        float(input("Second number: "))
                        )
                    )
            except ValueError:
                print("Error, not a valir number") 


        elif operation.lower() == 'b':


            try:
                print(
                    subtraction(
                        float(input("First number: ")),
                        float(input("Second number: "))
                    )
                )


        else:
            print("Invalid option, try again")    
    except ValueError:
        print("Invalid number, try again")


elif option.lower() == 'b':


    try:
        print("Option A to multiply")
        print("Option B to divide")


        operation = input("Choose an option: ")


        if operation.lower == 'a':


            try:
                print(
                    multiplication(
                        float(input("First number: ")),
                        float(input("Second number: "))
                    )
                )
            except ValueError:
                print("Error, not a valid number")


        elif operation.lower == 'b':


                try:
                    print(
                        division(
                            float(input("First number: ")),
                            float(input("Second number: "))
                        )
                    )
                except ValueError:
                    print("Error, not a valid number")
                except ZeroDivisionError:
                    print("Can't divide by zero")


            else:
                print("Invalid option, try again")
    except ValueError:
        print("Error, not a valid number")


elif option.lower() == 'c':


    try:
        print("Input 1 number")
        

        operation = float(input("Frist digit: "))


        if operation < 0:


            positive_operation = abs(operation)
            operation_2 = positive_operation ** 0.5
            print(f"{operation_2}j")
        

        else:
             operation_2 = operation ** 0.5
             print(operation_2)
    except ValueError:
        print("Error, not a valid number")


elif option.lower() == 'd':


    try:
        print(
            raise_to_power(
                int(input("First number: ")),
                int(input("Second number: "))
            )
        )
    except ValueError:
        print("Error, not a valid number")


else:
    print("Not a valid option, try again")
