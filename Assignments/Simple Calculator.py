def add(a, b):
    print(a + b) # runs the add function

num1 = input("pick a number\n> ") # has the user pick numbers to add
num2 = input("pick another number\n> ")
add(int(num1), + int(num2))

def subtact(x, y):
    print(x - y) # runs the subtraction function

sub1 = input("pick a number\n> ")  # has the user pick numbers to subtract 
sub2 = input("pick another number\n> ")
subtact(int(sub1), + int(sub2))

def multiply(w, z):
    print(w * z) # runs multiplication function

mult1 = input("pick a number\n> ") # has the user pick numbers to multiply
mult2 = input("pick another number\n> ")
multiply(int(mult1), + int(mult2))

def divide(r, t):
    print(r / t)  # runs diviton function

div1 = input("pick a number\n> ") # has the user pick numbers to divide
div2 = input("pick another number\n> ") 
divide(int(div1), + int(div2))

def exponet(u, i):
    print(u ** i) # runs the square funtion

exp1 = input("pick a number\n> ") # has the user pick a number to square
exp2 = input("pick a number to multiply via exponet\n> ")
exponet(int(exp1), + int(exp2))

def Moudulus(m, l):
    print(m%l)

first_number = input("pick a number\n> ")
divisor = input("pick another number\n> ")
Moudulus(int(first_number), int(divisor))