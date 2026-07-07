weight = float(input("Enter your weight in kilograms:"))
height = float(input("Eter your height in meters:"))
bmi = weight / (height * height)
print("your BMI is: ", format(bmi, '.2f'))