# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

rnum = round(random.random() * len(names)-1)

print(f"{names[rnum]} is going to buy the meal today!.")
