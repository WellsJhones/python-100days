print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

complete_name = name1+name2

t = complete_name.count("t")
r = complete_name.count("r")
u = complete_name.count("u")
e = complete_name.count("e")

true = t + r + u + e

l = complete_name.count("l")
o = complete_name.count("o")
v = complete_name.count("v")
e = complete_name.count("e")

love = l + o + v + e


total = int(str(true) + str(love))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
