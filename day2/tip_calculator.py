# bill value
bill = float(input('type the bill value: \n'))
# how many people will split the ill
people_split = int(input('enter how many people will split this bill: \n'))
# tip amount
tip = int(input('type the tip value: \n'))
tip = tip/100
tip_total = round((bill/people_split)*tip)
# each people will pay
total4each = bill / people_split+tip_total

print(f"Each peple shoud pay {total4each}$")
