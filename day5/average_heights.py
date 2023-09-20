students_heights = input("Input a list of heights").split()

# loop and split the values
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

# manual data
total_heights = 0
num_people = 0
for height in students_heights:

    total_heights += height
    num_people += 1

print("the media height is {}".format(rund(total_heights / num_people)))
