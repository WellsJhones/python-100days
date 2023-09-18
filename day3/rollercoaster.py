print("Wellcome to the rollercoaster!")

height = int(input("What's your heigh in cm? \n"))
# conditional statement
if height >= 120:
    print('You can ride the rollercoaster!')

    # check the age
    age = int(input("What is your age?"))

    if age < 12:
        bill = 5
        print('Child  pay $5.')
    elif age <= 18:
        bill = 7
        print('Youth pay $7')
    # free ride for people in age in range consider middle age crisis.
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult pay $12")
    whants_photo = input("Do you want a photo taken? Y or N.").upper()
    if whants_photo == 'Y':
        bill += 3
       # add $3 to the bill
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller to ride!")
