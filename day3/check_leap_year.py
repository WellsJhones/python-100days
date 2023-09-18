year = int(input("Which year do you want do check: \n"))

# if is clearly divisible for 4 is leap
if year % 4 == 0:
    # if is clearly for 100 is not leap
    if year % 100 == 0:
        # if is clearly divisible for 100 and 400 is leap
        if year % 400 == 0:
            print("is leap")
        else:
            print("not leap")
    else:
        print("is leap")
else:
    print("not leap")
