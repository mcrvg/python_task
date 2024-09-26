import random

magic_number=random.randint(1,100) # number randomly generated each time I play.
print(magic_number)
attempts=0
while attempts<5: #Allow 5 guesses
    guess=input("Guess a number between 1 and 100: ")
    if guess.isdigit():  # do not waste if I add not digits.
        guess = int(guess)
        attempts += 1
        n = 5 - attempts  # attempts left
        print("You have", n, "attempts left!!")

        if guess==magic_number:
            print(f"Congratulations! You guessed the number {magic_number} in {attempts} attempts.")
            break
        elif guess < magic_number:
            print("Too low. Try again.") ##know if I need to go higher or lower.
        else:
            print("Too high.Try again")
    else:
        print("Please enter a valid numerical guess.")
if attempts==5:
        print("Sorry, the game finish here")

print(f"The magic number was :{magic_number}")


