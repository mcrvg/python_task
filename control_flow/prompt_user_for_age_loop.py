#Input age
#age all digits
#check age is in the correct range<117

user_prompt=True
while user_prompt:
    age = input("What is your age? ")

    if age.isdigit() and int(age) < 117:
        user_prompt=False
        print(f"Your age is {age}")
    else:
        print("Please, enter a valid numerical age , and cannot be greater than 117")
        if age.isdigit() and int(age) < 117:
            user_prompt=False
            print(f"Your age is {age}")



















