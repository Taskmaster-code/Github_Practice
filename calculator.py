num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
operation = input("Enter a operation: ")

if operation == "+":
    print(num_1+num_2)
if operation == "-":
    print(num_1-num_2)
if operation == "*":
    print(num_1*num_2)
if operation == "/":
    if num_2 == 0:
        print("Not Defined")
    elif num_1 == 0:
        print("0")
    else:
        print(num_1/num_2)