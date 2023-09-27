import random
from art import logo

print(logo)


def get_card():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    return sum(cards)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        card.append(1)


def compare(userScore, computerScore):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "lose, opponent has blackjack"
    elif userScore == 0:
        return "win with a black jack"
    elif user_score > 21:
        return "you went over, you loose"
    elif computerScore == 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you loose"


is_game_over = False
user_cards = []
computer_card = []

for _ in range(2):
    user_cards.append(get_card())
    computer_card.append(get_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_card)
    print(" Your cars:{}, currrent socore: {}".format(user_cards, user_score))
    print(" Computer first card {} ".format(
        computer_card[0]))
    if user_cards == 0 or computer_score or user_score > 21:
        is_game_over = True
    else:
        new_card = input("type 'y' to get another card, type 'n' to pass: ")
        if new_card == "y":
            user_cards.append(get_card())
        else:
            is_game_over = True
while computer_score != 0 and computer_score < 17:
    computer_card.append(get_card())
    computer_score = calculate_score(computer_card)

print(compare(user_score, computer_score))
