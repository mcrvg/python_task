
# Get the user's height and weight68
weight=eval(input("Enter your weight in Kg"))
height=float(input("Enter your height in meters"))
# Calculate their BMI from the height and weight given
bmi = weight/float(height**2)

# Print the BMI as a message to the user
if bmi<18.5:
    print("Your BMI is",bmi,"and you are underweight you should gain weight")
elif bmi>=18.5 and bmi<=25:
    print("Your BMI is",bmi,"and your weight is normal, you should lose weight")
elif bmi>=25 and bmi<=30:
    print("Your BMI is",bmi,"and you are overweight you should lose weight")
else:
    print("Your BMI is", bmi, "and you have obesity")
#If time, create a version 2 with some of your own ideas
#tell them if they have to gain or lose weight to have normal BMI



