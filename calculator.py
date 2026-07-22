print("Addition of two numbers")
num1=float(input("first digit: "))
num2=float(input("second digit: "))
sum = num1+num2

print(sum)

print("Raise to power")
def raise_to_power(base_num, pow_num):
        result=1
        for index in range(pow_num):
                result = result * base_num
        return result

print(raise_to_power(int(input("1num: ")),int(input("2num: "))))
