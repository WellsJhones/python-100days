height = float(input("what's your height in M?"))
weight = int(input("what's your weight in Kg?"))
# calculate
bmi = weight / (height ** 2)
result = round(bmi)
# updated version 9/17/23

if result < 18.5:
    print(f"your BMI is {result}: you're underweight.")
elif result < 25:
    print(f"your BMI is {result}: you have a normal weight.")
elif result < 30:
    print(f"your BMI is {result}: you're overweight.")
elif result < 35:
    print(f"your BMI is {result}: you're obese.")
else:
    print(f"your BMI is {result}:you're clinical obese.")
