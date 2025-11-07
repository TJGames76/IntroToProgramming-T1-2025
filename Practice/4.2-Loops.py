

games = ["Elden Ring", "Diablo III" , "Minecraft", "Bo3", "PvZ 2"]

for game in games:
    print(game)

# Print every number from 1 -5 using a for loop

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

for i in range(0,5):
    print("Rank " + str(i ) + ":" +  games[i])

# Print every odd number from 1-100
'''
for i in range(0, 100, 10):
    print(i)

# Create a list of 100 random numbers that range from -100 to 100
# print only the positive numbers
import random
r = []
for i in range(0, 100):
    r.append(random.randint(-100, 101))

for i in range(0, len(r)):
    if r[i] < 0:
        r.pop(i)

print(r)
'''
count_down = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for num in count_down:
    print(num)

random_numbers = [5, 7, 8, 18, 6, 10, 7, 2, 10, 9]
sum = 0
for num in random_numbers:
   sum = sum + num 
print("Sum ", str(sum))

five_numbers = [4, 12, 20, 9, 7]
square_numbers = []
for square in five_numbers:
    square_numbers.append(square ** 2)
print(square_numbers)

string = input("Enter a word\n> ")
num_vowels = 0
for char in string:
    if char in ["a", "e", "i", "o", "u"]:
        num_vowels += 1 

print(num_vowels)

user_num = input("Enter an integer\n> ")
try:
    user_num = int(user_num)
except:
    print("Not an interger ...")
for i in range(1,10):
    print(str(user_num) + "x" + str(i) + " = " + str(user_num*i))

names = ["Tyler", "William" , "Noah", "Cole"]
for name in names:
    print("Hello, " + name + "!")