number_1 = float(input("Type your first number : "))
number_2 = float(input("Type your second number : "))
operator = input("Type your operator : ")
if (operator == "+"):
    print("%.2f"%(number_1 + number_2))

elif (operator == "-"):
    print("%.2f"%(number_1 - number_2))

elif (operator == "*"):
    print("%.2f"%(number_1 * number_2))

elif (operator == "/"):
    if (number_2 != 0 ):
        print("%.2f"%(number_1 / number_2))
    else:
        print ("Can't divide by 0!")
