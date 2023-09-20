for num in range(1, 101):
    # use a module to check, on this sequence is crucial to first declare division for 3 and 5 and only then each separeted.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
