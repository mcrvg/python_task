#Ask for details
weight=eval(input("Enter your weight in Kg"))
height=float(input("Enter your height in meters"))

#Calculate bmi
bmi = weight/float(height**2)

#Evaluate value of BMI, calculate w_n to have normal BMI
if bmi<=18.5:
    w=18.5*float(height**2)
    w_n=w-weight
    print("Your BMI is",bmi,"and you are underweight")
    print("To have normal BMI you need to gain at least",w_n,"Kg")
elif bmi>=18.5 and bmi<=25:
    print("Your BMI is", bmi, "and your weight is normal")
elif bmi>=25 and bmi<=30:
    w = 25 * float(height ** 2)
    w_n=weight-w
    print("Your BMI is", bmi, "and you are overweight")
    print("To have normal BMI you need to lose",w_n,"Kg")
else:
    w = 25 * float(height ** 2)
    w_n = weight - w
    print("Your BMI is", bmi, "and you have obesity")
    print("To have normal BMI you need to lose", w_n, "Kg")




