answer = ""
answer = input("Do you use standard parameters for weight and height? (Answer with:Yes/No)?:")

if answer == ("yes" or "Yes"):

    mass = float(input("Please enter your weight in Kg:"))
    height = float(input("Please enter your height in Meters:"))

    BMI = float(mass / (height ** 2))

    print("your Body Mass is:", BMI)

else:
    mass = float(input("Please enter your weight in pound:"))
    height = float(input("Please enter your height in inch:"))

    BMI = (mass / height ** 2) * 703
    print("your Body Mass is:", BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 < BMI < 25:
    print("Normal")
elif 25 < BMI < 30:
    print("Overweight")
else:
    print("Obesity")
