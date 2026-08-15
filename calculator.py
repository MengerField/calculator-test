#Simple calculator
#menger_2026


#Función para calcular la potencia de un número
def raise_to_power(base_num, pow_num):
    result = 1
    for _ in range(pow_num):
        result = result * base_num
    return result 


#Función para sumar
def addition(first_num, second_num):
    return first_num + second_num 


#Función para restar
def subtraction(first_num, second_num):
    return first_num - second_num 


#Función para multiplicar
def multiplication(first_num, second_num):
    return first_num * second_num 


#Función para dividir
def division(first_num, second_num):
    return first_num / second_num 


#Función main de la calculadora
def main():
    while True:
        print("Option A to addition or subtract")
        print("Option B to multiply or divide")
        print("Option C to get square root")
        print("Option D to raise to power")
        print("Type 'exit' to leave the program")
        option = input("Choose an option: ")

        if option.lower() == 'exit':
            break
        

        elif option.lower() == 'exit':
            break


        elif option.lower() == 'a':
            print("Option A to addition")
            print("Option B to subtraction")
            operation = input ("Choose an option: ")
            try:
                if operation.lower() == 'a':
                    print(
                        addition(
                            float(input("First number: ")),
                            float(input("Second number: "))
                        )
                    )
                elif operation.lower() == 'b':
                    print(
                        subtraction(
                            float(input("First number: ")),
                            float(input("Second, number: "))
                        )
                    )
                else:
                    print("Invalid option, try again")
            except ValueError:
                print("Error, not a valid number")
            
        
        elif option.lower() == 'b':
            print("Option A to multiply")
            print("Option B to divide")
            operation = input("Choose an option: ")
            try:
                if operation.lower() == 'a':
                    print(
                        multiplication(
                            float(input("First number: ")),
                            float(input("Second number: "))
                        )
                    )
                elif operation.lower() == 'b':
                    try:
                        print(
                            division(
                                float(input("First number: ")),
                                float(input("Second number: "))
                            )
                        )
                    except ZeroDivisionError:
                        print("Can't divide by zero")
                else:
                    print("Invalid option, try again")
            except ValueError:
                print("Error, not a valid number")


        elif option.lower() == 'c':
            try:
                print("Input 1 number")
                number = float(input("First digit: "))
                if number < 0:
                    result = abs(number) ** 0.5
                    print(f"{result}j")
                else:
                    result = number ** 0.5
                    print(result)
            except ValueError:
                print("Error, not a valid number")

        elif option.lower() == 'd':
            try:
                print(
                    raise_to_power(
                        int(input("Base number: ")),
                        int(input("Exponent: "))
                    )
                )
            except ValueError:
                print("Error, not a valid number")
            

        else:
            print("Not a valid option, try again")

                
if __name__ == '__main__':
    main()
