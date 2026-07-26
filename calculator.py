#   GNU nano 7.2                      calculator.py
print("Option A to addition or substrac")
print("Option B to raise to power")
print("Option C to multiply")
option=(input("Choose an option: "))
if option.lower()=="a":
        print("Input 2 numbers")
        num1=float(input("first digit: "))
        num2=float(input("second digit: "))
        print("Option A to addition")
        print("Option B to subtraction")
        option2=(input("Choose an option: "))
        if option2.lower()=="a":
                sum = num1+num2
                print(sum)
        else:
                res = num1-num2
                print(res)
elif option.lower()=="c":
        print("Input 2 numbers")
        fnum=float(input("first digit: "))
        snum=float(input("second digit: "))
        print("Option A to multiply")
        print("Option B to divide")
        op3=(input("Choose an option: "))
        if op3.lower()=="a":
                mult = fnum*snum
                print(mult)
        else:
                div = fnum//snum
                print(div)
else:
        print("Raise to power")
        def raise_to_power(base_num, pow_num):
                result=1
                for index in range(pow_num):
                        result = result * base_num
                return result

        print(raise_to_power(int(input("1num: ")),int(input("2num: "))))
