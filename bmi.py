height=float(input("Enter your height in cm "))
weight=float(input("Enter your weight in kg "))
bmi=weight/(height/100)**2
if bmi<=18.4:
    print("You are underweight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are overweight")
else:
    print("You are obese")