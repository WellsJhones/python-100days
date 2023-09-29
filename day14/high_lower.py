import random
from art import logo, vs
from game_data import data
print(logo)

# Shuffle the data list to randomize the order of the entities
random.shuffle(data)

# Pick the first entity in the shuffled list as the starting entity
current_entity = data[0]

# Keep track of the player's score
score = 0

# Game loop
while True:
    # Print the current entity's information
    print(
        f"Compare A: {current_entity['name']}, a {current_entity['description']} from {current_entity['country']}")

    # Print the vs. separator
    print(vs)

    # Pick a random entity from the data list as the opponent
    opponent_entity = random.choice(data)

    # Make sure the opponent is not the same as the current entity
    while opponent_entity == current_entity:
        opponent_entity = random.choice(data)

    # Print the opponent's information
    print(
        f"Against B: {opponent_entity['name']}, a {opponent_entity['description']} from {opponent_entity['country']}")

    # Ask the player to guess which entity has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check the player's guess and update the score
    if guess == 'a' and current_entity['follower_count'] > opponent_entity['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    elif guess == 'b' and current_entity['follower_count'] < opponent_entity['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    # Set the opponent entity as the new current entity for the next round
    current_entity = opponent_entity
