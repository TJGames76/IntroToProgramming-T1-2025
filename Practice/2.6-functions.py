def greet():
     # indented lins are inside the fucntion
    print("Hello World!")
    print("This is the second line!!")
    print("This is the third line!!!!")
#the function ends here
print("Hmmm...") # not indented -> no in function!


greet()
 
#Create a fucntion that adds two numbers togeather
def add(x, y):
    print(x+y)


add(10,30)

def calculate_tax(iteam, price, rate):
    print("The amoun of tax to be colected on a " + str(price) + "dollar" +iteam + " is " + str(.1*price*rate))

calculate_tax("Starbucks", 7.99, 0.6825)

def add_five_numbers(a, b, c, d, e):
    print((a) + (b) + (c) + d + e)

add_five_numbers(5, 10, 30, 40, 5)


def full_name(first, last):
    print(first + " " +last)
   
    

first_name = input("enter your first name\n> ")
last_name = input("enter your last name\n> ")

full_name(first_name, last_name)


def area_calculator(length, width):
    print(length*width)

area_calculator(35, 40)
area_calculator(16, 27)
area_calculator(15, 98)

def word_smash(a, b):
    print(str(a) + str(b))

word_smash("cat", "dog")



def echo(x, y):
    print(str(x) * y)

echo("bob", 7)

def happy_birthday(name):
    print("Happy Birthday to " + name + " Happy Birthday to " + name + " Happy bithday to " + name + " Happy Birthday tooooo " + name)
happy_birthday("Tyler")