
import random
def dice_game():
    """A simple dice game where the user and the computer roll a dice until one reaches 30 points. The first to reach 30 wins."""

    print("Welcome to the Dice Game!")
    name = input("Please enter your name: ")

    user_score = 0
    computer_score = 0

    while user_score < 30 and computer_score < 30:
        print(f"\n{name}'s score: {user_score} | Computer's score: {computer_score}")
        input("Press Enter to roll the dice...")

        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print(f"{name} rolled: {user_roll}")
        print("Computer rolled: {computer_roll}")

        user_score += user_roll
        computer_score += computer_roll

    if user_score >= 30:
        print(f"\nCongratulations, {name}! You won with a score of {user_score}.")
    else:
        print("\nThe computer won! Better luck next time.")

    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        dice_game()

if __name__ == "__main__":
    dice_game()