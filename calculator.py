#   GNU nano 7.2                      calculator.py
banana = 0
while banana == 0 :
        mango=input("exit to end the program or enter to start: ")
        if mango.lower() == 'exit' :
                banana = 1
                break
        print("Option A to addition or substrac")
        print("Option B to multiply or divide")
        print("Option C to get root square")
        print("Option D to raise to power")
        option=(input("Choose an option: "))
        if option.lower()=="a":
                try:
                        print("Input 2 numbers")
                        num1=float(input("first digit: "))
                        num2=float(input("second digit: "))
                        print("Option A to addition")
                        print("Option B to subtraction")
                        option2=(input("Choose an option: "))
                        if option2.lower()=="a":
                                add = num1+num2
                                print(add)
                        elif option2.lower()=="b":
                                res = num1-num2
                                print(res)
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
                                div = fnum/snum
                                print(div)
                        else:
                                print("Invalid option, autodestruccion in 3...2...1...")
                except ValueError:
                        print("Error not a valid number")

        elif option.lower()=="c":
                try:
                        print("Input 1 number")
                        rnum=(float(input("first digit: ")))
                        op3=rnum**0.5
                        print(op3)
                except ValueError:
                        print("Error, not a valid number")

        elif option.lower()=="d":
                try:
                        print("Raise to power")
                        def raise_to_power(base_num, pow_num):
                                result=1
                                for index in range(pow_num):
                                        result = result * base_num
                                return result
                        print(raise_to_power(int(input("1num: ")),int(input("2num: "))))
                except ValueError:
                        print("Error, no valid number")
        else:
                 print("No valid option, autodestruction in 3...2...1...")
        
