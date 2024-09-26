#Use your code from the "Task: Get name, age and DOB details from a user".

age=int(input("Hi\nEnter your age by the end of 2024"))
name=input("Enter your name")
year=2024-age
#Mix the name, age and DOB into one list user_details_list
user_details=[age,name,year]
#Print the user's name, age and DOB from the list
print(user_details)
#If age it's not int, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details[0]))
#Ask the user for their height in cm and save it to the variable height

#Save height as a float in the list, and print the height from the list.
########height=user_details.append(float(input("Enter your height in meters")))
#####print(user_details)


