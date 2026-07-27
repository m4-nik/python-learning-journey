print ("Hello viewer, I have created this code to find compound interest!")
principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Please enter the principal amount: "))
    if principle <=0:
        print ("This is not a valid principal amount.")

while rate <=0:
    rate = float(input("Please enter the rate of interest: "))
    if rate <=0:
        print ("This is not a valid rate.")

while time <=0:
    time = float(input("Please enter the time: "))
    if time<=0:
        print ("This is not a valid time, please enter it in years.")

print (f"So your principle is ${principle}, rate is {rate}% and time is {time} years.")

amount = principle * pow(1 + rate/100 , time)

print(f"So the final amount is ${amount:.2f}!")





print ("Hello viewer, I have created this code to find compound interest!")
principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Please enter the principal amount: "))
    if principle <=0:
        print ("This is not a valid principal amount.")

while rate <=0:
    rate = float(input("Please enter the rate of interest: "))
    if rate <=0:
        print ("This is not a valid rate.")

while time <=0:
    time = float(input("Please enter the time: "))
    if time<=0:
        print ("This is not a valid time, please enter it in years.")

print (f"So your principle is ${principle}, rate is {rate}% and time is {time} years.")

amount = principle * pow(1 + rate/100 , time)

print(f"So the final amount is ${amount:.2f}!")





