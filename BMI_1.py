mass = float(input("Please enter your weight in Kg:"))
height = float(input("Please enter your height in Meters:"))

BMI = mass / (height * height)

if BMI < 18.5:
    print("Underweight")
elif 18.5 < BMI < 25:
    print("Normal")
elif 25 < BMI < 30:
    print("Overweight")
else:
    print("Obesity")

print("your Body Mass is:", BMI)