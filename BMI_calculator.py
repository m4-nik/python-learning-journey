#BOSS FIGHT - BMI
print ("This program is designed to check your Body Mass Index.")
weight = float(input("Please enter your weight in kilograms."))
height = float(input("Please enter your height in meters."))

BMI = weight / (height * height)
BMI = round(BMI, 2)
print (BMI)

if BMI < 18.5:
    print("Category: Underweight")
    print("It's time for you to eat more sweetheart.")
elif 18.5 <= BMI < 25:
    print("Category: Normal weight")
    print("You are perfect! Keep it up.")
elif 25 <= BMI < 30:
    print("Category: Overweight")
    print("Time to go to gym bro!")
elif BMI > 30:
    print("Category: Obese")
    print("Health check recommended.")
else:
    print("Enter a valid weight to continue")




