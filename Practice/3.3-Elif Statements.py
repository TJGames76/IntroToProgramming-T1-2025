Word_1 = input("enter a sentence in all lower case\n> ")
Word_2 = "Your Dad"
print(str.upper(Word_1))
print(str.strip(Word_1))
print(Word_1.replace("bad", "good"))

if Word_1.endswith("."):
    print(True)
else:
    print(False)



#Coin sorter

coin_diameter = "" 
deposit = 0.00

if 