try:
    # Code that may raise an exception
    numerator = 10 
    denominator = 0
    result = numerator / denominator
except:
    # Code to hable the exception
    print("Error: Cannot divide by zero.")


def times_two():

    num = input("Enter a number\n> ")

    try:
      print(int(num) * 2)
    except:
        print("You must enter a integer")
        times_two()

times_two()

import random

r = random.randint(0,10)

print(r)
