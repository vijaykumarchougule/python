# We are creating the SimpleCalulator Using Switcher where we can calculate +, -, *, /, %.

print("!!!--- Welcome To SimpleCalculator ---!!!\n")


def switchCase(num1, num2, val):
    switcher = {
        1: "The addition of {0} and {1} is {2}".format(num1, num2, num1+num2),
        2: "The substraction of {0} and {1} is {2}".format(num1, num2, num1-num2),
        3: "The multiplication of {0} to {1} is {2}".format(num1, num2, num1*num2),
        4: "The division of {0} by {1} is {2}".format(num1, num2, num1/num2),
        5: "The remainder of {0} of {1} is {2}".format(num1, num2, num1 % num2),

    }

    return switcher.get(val)


if __name__ == "__main__":
    while(1):
        print("\nEnter the Two numbers: ")
        num1 = float(input("1st Number: "))
        num2 = float(input("2st Number: "))
        print("Enter 1=> +, 2=> -, 3=> *. 4=> /, 5=> %.\n")
        val = int(input("Enter Your Choice"))
        print(switchCase(num1, num2, val))
