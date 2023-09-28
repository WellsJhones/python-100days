import random
from art import logo


def play_game():
    print(logo)

    choose_the_dificult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_the_dificult == "easy":
        lifes = 10
    elif choose_the_dificult == "hard":
        lifes = 5
    else:
        print("Invalid difficulty")
        return

    print(f"You have {lifes} attempts remaining to guess the number.")
    random_number = random.randint(1, 100)

    while lifes > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        lifes -= 1
        print(f"You have {lifes} attempts remaining to guess the number.")

    print(f"Game over. The answer was {random_number}.")


while True:
    play_game()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if play_again != "yes":
        break
