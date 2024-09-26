
# Calculate year of birth
from calendar import timegm

age=int(input("Enter your age by the end of 2024"))
name=input("Enter your name")
year=2024-age
print("OMG","name", "you are",age," years old so you were born in",year)

#calculate and print out the total number of hours this person has lived
hours=365*24*age
print("name","will have live",hours,"hours by the end of 2024")