import random
print("Welcome to the game ")
# using easy way
options = ['rock', 'paper', 'scissor']
random_num = random.choice(options)

# second way
random_num = round(random.random()*2)
random_choice = options[random_num]
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img = [rock, paper, scissors]
# user choice
user_choice = int(input(
    "What's type a number to select your choice: '0 Rock', '1 Paper' or '2 Scissor' \n"))

if user_choice == random_num:
    print(
        f"{img[user_choice]}\n computer choose {img[random_num]} \n It's a draw! ")
elif user_choice == 0 and random_num == 1:
    print(
        f"{img[user_choice]}\n computer choose {img[random_num]}You loose ")
elif user_choice == 1 and random_num == 2:
    print(
        f"{img[user_choice]}\n computer choose {img[random_num]}You loose ")
elif user_choice == 2 and random_num == 0:
    print(
        f"{img[user_choice]}\n computer choose {img[random_num]}You loose ")
else:
    print(
        f" {img[user_choice]}\n computer choose {img[random_num]}\nCongratulation you WIN!!!! ")
