'''

if condition:
    # Code to execute if the condition is true

else:
    # needs and if statment
    #if the condition of the if statment fails the else statment will print

    '''

number = 5

if number > 0:
    print("The number is positive")

number = -3

if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")

a = 0
b = 11
c = 52


if a < 0 or b == 10:
    print("kiwi")

else:
    print("plum")

real_password = "Knights25"
submitted_password = "knights25"

if real_password == submitted_password:
    print("enter")

else:
    print("fail")



def check_password():
 Real_password = "Timtom67"
 password = input("enter password\n> ")

 if Real_password == password:
    print("acesses granted")
 else:
    print("acesses not granted" )
    check_password()


check_password()

age = 20     # if inside of if statments
has_premission = True

if age >= 18:
    if has_premission:
        print("Access granted")
    else:
        print("Access denied: Premission required")
else:
    print("Acsses denied: age restriction")