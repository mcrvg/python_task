
for number in range(1, 100): #numbers from 1 to 100.
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


    """Prints numbers from start to end, replacing multiples of fizz_multiple with "Fizz"
     and multiples of buzz_multiple with "Buzz".

    Args:
        start (int): The starting number.
        end (int): The ending number.
        fizz_multiple (int): The multiple for which to print "Fizz".
        buzz_multiple (int): The multiple for which to print "Buzz".
    """

    for number in range(start, end):
        if number % (fizz_multiple * buzz_multiple) == 0:
            print("FizzBuzz")
        elif number % fizz_multiple == 0:
            print("Fizz")
        elif number % buzz_multiple == 0:
            print("Buzz")
        else:
            print(number)
