# BMI caculator
w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))
bmi = w/(h*h)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("you are healthy")
elif bmi < 30:
    print(" you are Overweight")
else:
    print("you are Obese")