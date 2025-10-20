import random
def fourtune_teller():
    print("Hi I am the fortune teller and i will take a imput of intgers to tell your fortune")
    luck = 0
    Lucky_number = input("Enter your lucky number as a integer\n> ")
    if int(Lucky_number) >= 50:
        luck = luck - 1
    else:
        luck = luck + 1
    future = input("As a integer enter how many years you what me to see into the future\n> ")
    if future <= "10":
        luck = luck - 1
    else:
        luck = luck + 1
    age = input("Enter your age as a integer\n> ")
    if age >= "35":
        luck = luck - 1
    else:
        luck = luck + 1
    print(int(luck)) 
    print("luckyness out of 3")
fourtune_teller()