
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = 0
for max in student_scores:
    if max > highest_score:
        highest_score = max


print("The highest score in the class is: {}".format(highest_score))
