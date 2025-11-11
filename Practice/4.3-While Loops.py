# while condition:
    # code to repeat
'''
num = 0 

while num < 100:
    num += 1
    print(num)

num = 0 
continue_adding = True
while continue_adding == True:
    num += 1
    print(num)
    ask = input("Whould you like to continue? Y/N\n> ")
    if ask.lower() == "n":
        continue_adding = False
'''
import random
def random_number_gen():
    random_number = random.randint(0, 100)
    guess = int(input("Guess a number 1-100\n> "))
    end_loop = True
    while end_loop == True and guess > random_number:
        print("Lower!")
        guess = int(input("Guess a number 1-100\n> "))
        if end_loop == True and guess < random_number:
            print("Higher")
            guess = int(input("Guess a number 1-100\n> "))
        elif end_loop == True and guess ==  random_number:
            print("Correct")
            end_loop = False
random_number_gen()

