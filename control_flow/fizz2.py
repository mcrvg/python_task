
start=int(input("Start number of the game,"))
end=int(input("End number of the game"))
fizz_multiple=int(input("Choose Fizz Multiple"))
buzz_multiple=int(input("Choose Buzz Multiple"))

for number in range(start,int(end)+1):
    if number % (fizz_multiple*buzz_multiple) == 0:
        print("FizzBuzz")
    elif number % fizz_multiple == 0:
        print("Fizz")
    elif number % buzz_multiple == 0:
        print("Buzz")
    else:
        print(number)