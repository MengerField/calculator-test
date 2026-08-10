#   GNU nano 7.2                      calculator.py
def raise_to_power(base_num, pow_num):
        result=1
        for index in range(pow_num):
                result = result * base_num
        return result
def addition(first_num, second_num):
    result=first_num+second_num
    return result

def substrac(first_num, second_num):
    result=first_num-second_num
    return result
def multiplication(first_num, second_num):
        result=first_num**secon_num
        return result
def division(first_num, second_num):
        result=first_num/second_num
        return result

while True :
        CodeGeass=input("Press any key to start or exit to leave the program: ")
        if CodeGeass.lower() == 'exit' :
                break
        print("Option A to addition or substrac")
        print("Option B to multiply or divide")
        print("Option C to get root square")
        print("Option D to raise to power")
        option=(input("Choose an option: "))
        
        if option.lower()=="a":
                try:
                        print("Option A to addition")
                        print("Option B to subtraction")
                        option2=(input("Choose an option: "))
                        if option2.lower()=="a":
                                try:
                                     print(addition(float(input("First number: ")),float(input("Second number: "))))
                                except ValueError:
                                        print("Error, not a valid number")
                        elif option2.lower()=="b":
                                try:
                                     print(substrac(float(input("First number: ")),float(input("Second number: "))))
                                except ValueError:
                                        print("Error, not a valid number")
                        else:
                                print("Invalid option, autodestruccion in 3...2...1...")
                except ValueError:
                        print("Error, not a valid number")
        elif option.lower()=="b":
                try:
                        print("Input 2 numbers")
                        fnum=float(input("first digit: "))
                        snum=float(input("second digit: "))
                        print("Option A to multiply")
                        print("Option B to divide")
                        op3=(input("Choose an option: "))
                        if op3.lower()=="a":
                                mult = fnum*snum
                                print(mult)
                        elif op3.lower()=="b":
                                try:
                                        div = fnum/snum
                                        print(div)
                                except ZeroDivisionError:
                                        print("No mames we no se puede divir por cero")
                        else:
                                print("Invalid option, autodestruccion in 3...2...1...")
                except ValueError:
                        print("Error not a valid number")

        elif option.lower()=="c":
                try:
                        print("Input 1 number")
                        rnum=(float(input("first digit: ")))
                        if rnum<0:
                                prnum=abs(rnum)
                                op3=prnum**0.5
                                print(f"{op3}j")
                        else:        
                                op3=rnum**0.5
                                print(op3)
                except ValueError:
                        print("Error, not a valid number")

        elif option.lower()=="d":
                try:
                        print("Raise to power")
                        print(raise_to_power(int(input("1num: ")),int(input("2num: "))))
                except ValueError:
                        print("Error, no valid number")
        else:
                 print("No valid option, autodestruction in 3...2...1...")
