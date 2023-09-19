
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# select row, get the correct range we reduce 1
horizontal = int(position[0])-1
vertical = int(position[1])-1
# change the value of the position
map[vertical][horizontal] = "x"

print(f"{row1}\n{row2}\n{row3}")
