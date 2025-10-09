answer_1 = "67"
quetion_1 = input("What is 10 + 57\n> ")

answer_2 = "64"
quetion_2 = input("What is 8 * 8\n> ")

answer_3 = "100"
quetion_3 = input("What is 10 squared\n> ")

answer_4 = "-5"
quetion_4 = input("What is 5 - 10\n> ")

answer_5 = "5"
quetion_5 = input("What is 25 / 5\n> ")

def tally_score():
    if quetion_1 == answer_1:
        print("Correct")
        a = 1
    else:
        print("Incorrect")
        a = 0
    if quetion_2 == answer_2:
        print("Correct")
        b = 1
    else:
        print("Incorrect") 
        b = 0
    if quetion_3 == answer_3:
        print("Correct")
        c = 1
    else:
        print("Incorrect")
        c = 0
    if quetion_4 == answer_4:
        print("Corrcet")
        d = 1
    else:
        print("Incorrect")
        d = 0
    if quetion_5 == answer_5:
        print("Correct")
        e = 1
    else:
        print("Incorrect")
        e = 0
    print("Score" + str(a + b + c + d + e) + "/5")
tally_score()