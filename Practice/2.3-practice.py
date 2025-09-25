# String    - "in quotations"
# Integer   - a whole number ex. 1 4 -10 ect.
# Float     - a decimal nimber ex 3.1415765989
# Char      - a single glyph ex.  'c'
# BooL      - True or False

# How to define a variable!!
# <name> = <value>

lowercase = False
UPPERCASE = False
UpperCamelCase = False   #ALL lowercase, no spaces, capital for new words
lowerCamelCase = False   #ALL lowercase, no spaces, capital for new words
snake_case = True        #All lowercase, underscores for spaces
TrueSCREAMING_SNAKE_CASE = False

# Other general rules to naming things
# 1. Concise
#  -

the_font_size_for_paragrahps = 10
font_size_para = 10
para_size = 10
para = 10

name = input ("What is your name?\n>")
#\n is a short cut to move text down a line (escape charcter)
print ("Your name is " + name) 

#Get the numver as a string
num = input("what number do you want to square?\n> ")

#Parse (convert) the string to an integer
num = int(num)
#int turns string into a number can you can do the same with flots and the others

#Do math and print
print(num * num)