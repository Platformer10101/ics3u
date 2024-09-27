weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in Meters: "))
BMI = weight / (height ** 2)

print(f"Your BMI is {BMI}")

weight = float(input("Enter your weight in lbs: "))
height = float(input("Enter your height in Inches: "))
BMI = 703 * (weight / (height ** 2))

print(f"Your BMI is {BMI}")

weight = float(input("Enter your weight in Kg: "))
heightf = float(input("Enter your height (feet only): "))
heighti = float(input("Enter your height (inches only): "))
BMI = 703 * (weight / (((12 * heightf ) + heighti) ** 2))

print(f"Your BMI is {BMI}")


