import random
from word_list import word_list

random_choice = random.choice(word_list)
print(random_choice)
print("Welcome to the Hang Man game")
print("choose a letter")

life = 6
guessed_letters = []

end_game = False
for _ in range(len(random_choice)):
    guessed_letters += "_"
if not life > 0:
    end_game = True
print(guessed_letters)
while not end_game:
    if "_" not in guessed_letters:
        print("you win")
        end_game = True

    user_choice = input().lower()
    if user_choice in guessed_letters:
        print("this letter was gessed, try another \n")
    for letter in range(len(random_choice)):
        if random_choice[letter] == user_choice:
            guessed_letters[letter] = user_choice
            print(guessed_letters)
    if user_choice not in random_choice:
        life -= 1
        print("don't have, you have only {} lives".format(life))
        if life == 0:
            end_game = True
            print("you loose")
