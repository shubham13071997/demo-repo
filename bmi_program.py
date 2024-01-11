
print("Welcome to Body Mass Index Calculator")
weight = input("Enter your weight(kg) - ")
height = input("Enter your height(m)- ")

BMI= float(weight)/(float(height)** 2)

BMI= round(BMI,5)
print(BMI)

if BMI <=16:
 print("Body is underweight")

elif BMI>16 and BMI<24:
    print("BMI is Normal")

else:
    print('Body is overweight')