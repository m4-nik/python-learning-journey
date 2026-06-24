#over here we are trying to write a code for a calculator using if statements

print ("Hello buddy, welcome to python.")
print ("Lets make a calculator today :) ")
operator = input("So you wanna +,-,* or / ?")
print ("Alright")
print (repr(operator))
number1 = float (input("Enter the first number"))
number2 = float (input("Enter the second number"))

if operator =="+":
    result = number1 + number2
    print (round(result , 2))
elif operator =="-":
    result = number1 - number2
    print (round(result , 2))
elif operator =="*":
    result = number1 * number2
    print (round(result , 2))
elif operator =="/":
    result = number1 / number2
    print (round(result , 2))
else:
    result = ("no answer")
    print(f"Invalid operator as {operator} is not valid, nice try to fool me :) ")

print (f"So your chosen option gave us {result}. Thanks for using me hehe")




