#GNU nano 7.2                      calculator.py                               
print("Option A to addition of 2 numbers")
print("Option B to raise to power")

option=(input("Choose an option: "))
if option.lower()=="a":
        print("Input 2 humbers")
        num1=float(input("first digit: "))
        num2=float(input("second digit: "))
        print("Option 1 to addition")
        print("Option 2 to substraction")
        option2=(input("Choose an option: "))
        if option2.lower()=="a":
                sum = num1+num2
                print(sum)
        else:
                res = num1-num2
                print(res)
else:
        print("Raise to power")
        def raise_to_power(base_num, pow_num):

