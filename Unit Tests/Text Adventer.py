# 2 = sword
# 3 = armor
# 4 = heal
def start_adventure():
    print("")
    print("You find yourself walking around a vilage on your adventure when you come across the vilages forest.")
    print("In this world of adventures there are diffrent areas to slay monsters and the forest is the base level.")
    print("As you stand at the foot of the forest you think of what to do.")
    print("1. You decide to enter blindly.")
    print("2. You head back for the day")
    print("3. You decide to ask around for info.")
    print("4. You stand there and look stupid.")
    
    choice_1 = input("What would you do\n> ")
    
    if choice_1 == "1":
        enter_forest()
    elif choice_1 == "2":
        return_home()
    elif choice_1 == "3":
        ask_for_info()
    elif choice_1 == "4":
        look_stupid()
    else:
        print("Invalid choice. Try again")
        start_adventure()
# Part 1    
def enter_forest():
    print("you enter the forest and head to the right. as you wander deeper into the outer layer you happen across a monsters nest. What do you do.")
    print("1. take a stealthy aproche.")
    print("2. walk away.")
    print("3. Stand there till they notice you.")
        
    choice_2a = input("What would you do\n> ")
    
    if choice_2a == "1":
        stealth()
    elif choice_2a == "2":
        walk_away()
    elif choice_2a == "3":
        stay()
    else:
        print("Invalid choice. Try again")
        enter_forest()
    

def return_home():
    print("You return home and think today is not the day and hit the sack.")
    print("You wake up the next day and are ready to start the day off fresh.")
    print("You can")
    print("1. get dressed and head out for food")
    print("2. stay in bed")
    
    choice_2b = input("What would you do\n> ")
    
    if choice_2b == "1":
        get_dressed()
    elif choice_2b == "2":
        stay_in_bed()
    else:
        print("Invalid choice. Try again")
        return_home()


def ask_for_info():
    print("You chose to ask some villagers if they know any thing about the forest.")
    print("One villager tells you that there are rings to the forest and that the further you head in the harder it gets and then she hands you a map")
    print("What would you do.")
    print("1. head into the eaiser part of the forest.")
    print("2. You chose to rush right in.")
    print("3. You head into a shop in hope to fined some cheap gear to use.")
    print("4. You are to scaerd and don't what to fight.")
    
    choice_2c = input("What would you do\n> ")
    
    if choice_2c == "1":
        enter_forest()
    elif choice_2c == "2":
        rush_in()
    elif choice_2c == "3":
        shop()
    elif choice_2c == "4":
        ending_2()
    else:
        print("Invalid choice. Try again")
        ask_for_info()
    
def look_stupid():
    print("you look stupid ... Try again")
    print("")
    start_adventure()
# Part 2a
def stealth():
    print("You decied to sneak up on the monsters the closer you draw near they still  don't see you.")
    print("What would you do")
    print("1. Draw your fist and fight.")
    print("2. Sneak by.")
    print("3. Turn back and leave.")
    
    choice_3a = input("What would you do\n> ")
    
    if choice_3a == "1":
        fist_fight()
    elif choice_3a == "2":
        Sneak_by()
    elif choice_3a == "3":
        return_home()
    else:
        print("Invalid choice. Try again")
        stealth()

def walk_away():
    print("you decied to head to the left untill you happen apon a cave.")
    print("What do you want to do")
    print("1. Enter the cave.")
    print("2. walk around the cave")
    print("3. Head back to fight the nest you saw earlier")
    print("4. Your to sacred to fight at all and call it quits")
    
    choice_3b = input("What would you do\n> ")
    
    if choice_3b == "1":
        Enter_cave()
    elif choice_3b == "2":
        Walk_around()
    elif choice_3b == "3":
        enter_forest()
    elif choice_3b == "4":
        ending_2()
    else:
        print("Invalid choice. Try again")
        walk_away()

def stay():
    print("What did you think would happen")
    ending_1()
# Part 2b
def get_dressed():
    print("So you decied to get ready and head out for the day.After getting a bite to eat you think of what you want to do next ")
    print("1. Head In to the forest.")
    print("2. Enter a Shop to get some gear")
    print("3. stand there and look stupid")
    
    choice_3d = input("What do you want to do\n> ")
    
    if choice_3d == "1":
        enter_forest()
    elif choice_3d == "2":
        shop()
    elif choice_3d == "3":
        look_stupid()
    else:
        print("Invalid choice. Try again")
        get_dressed()

def stay_in_bed():
    print("")
    print("")
    print("")
    print("")
    print("How long do you plan to stay here. Get up!")
    print("")
    get_dressed()
#Part 2c
def rush_in():
    print("after find out this info you want to rush in to get center to get more money and strength quicker")
    ending_1()
    
def shop():
    print("You enter a near by shop to get some gear.")
    print("As you look at the prices on the wall you realise you don't have alot of money to get any of the good gear")
    print("you walk over the the cheap gear and take a look around")
    print("You have $100 what would you like to by")
    print("1. a rusty sword for $75")
    print("2. a full set of rusty armor $100")
    print("3. a bottom less heath potion for $50")
    print("4. leave")
    
    choice_3e = input("What would you like to do\n> ")
    
    if choice_3e == "1":
        print("you now have a rusty sword")
        leave_1()
    elif choice_3e == "2":
        print("you now have a full set of rusty armor")
        leave_2()
    elif choice_3e == "3":
        print("you now have a health potion")
        leave_3()
    elif choice_3e == "4":
        print("you don't buy anything and ")
        leave_4()
    else:
        print("Invalid choice. Try again")
        shop()

# ending_3
def ending_3():
    print("you have found the hidden ending. You are completly lost")
    
    #ending_2
def ending_2():
    print("You chose to give up ... How boring")
    ending_1b = input("Would you like to start over (yes or no)\n> ")
    if ending_1b == "yes":
        start_adventure()
    elif ending_1b == "no":
        print("Lame")
    else:
        print("Invalid choice. Try again")

#ending_1
def ending_1():
    print("")
    print("How well did that work out for you. You are now dead due to your dumb choices. Better luck next time")
    
    ending_1 = input("Whould you like to try again (yes or no)\n> ")
    if ending_1 == "yes":
        start_adventure()
    elif ending_1 == "no":
        print("Lame")
    else:
        print("Invalid choice. Try again")
        ending_1()
def ending_1b():
    print("")
    print("Nice one ...   You missed, i mean what did you expect jumping on monster with your fist would do")
    print("I mean common realy.")

    ending_1 = input("Whould you like to try again (yes or no)\n> ")
    if ending_1 == "yes":
        start_adventure()
    elif ending_1 == "no":
        print("Lame")
    else:
        print("Invalid choice. Try again")
        ending_1b()
def ending_1c():
    print("All you had was your fist what were you going to do, play patty cake.")
    print("")
    print("Your dead")
    print("")
    
    ending_1 = input("Whould you like to try again (yes or no)\n> ")
    if ending_1 == "yes":
        start_adventure()
    elif ending_1 == "no":
        print("Lame")
    else:
        print("Invalid choice. Try again")
        ending_1c()
#Part 3a 
def fist_fight():
    print("You deside to fight with fist")
    print("Would you like to")
    print("1. rush right in")
    print("2. go for a jump attack")
    print("3. sneak up from the back")
    print("4. search the area")

    choice_4a = input("What would you do\n> ")

    if choice_4a == "1":
        ending_1()
    elif choice_4a == "2":
        ending_1b()
    elif choice_4a == "3":
        ending_1c()
    elif choice_4a == "4":
        search()
    else:
        print("Invalid choice. Try again")
        fist_fight()
def Sneak_by():
    print("You choice to sneak by ")
    print("good luck hope fully you don't step on a stick and make a bunch of noise to draw the monster atention righttttttttttttttttttttttttttttttttttttt")
    print("You made to much noise when trying to sneak by and got killed")
    
    ending_1 = input("Whould you like to try again (yes or no)\n> ")
    
    if ending_1 == "yes":
        start_adventure()
    elif ending_1 == "no":
        print("Lame")
    else:
        print("Invalid choice. Try again")
        Sneak_by()

# Part 3b
def Enter_cave():
    print("You deiced to enter the near by cave")
    print("Do you want to.")
    print("1. Enter in further")
    print("2. Leave")
    print("3. Look around")

    choice_4b = input("What do you want to do\n> ")

    if choice_4b == "1":
        enter_deeper()
    elif choice_4b == "2":
        Leave_cave()
    elif choice_4b == "3":
        print("")
        print("like the view")
        print("")
        Enter_cave()
    else:
        print("Invalid choice, Try again")

def Walk_around():
    print("You finaly make it around the cave and find your self at the edge of a cliff.")
    print("Do you want to")
    print("1. Turn back and enter cave")
    print("2. Look around")
    print("3. Jump")

    choice_4c = input("What do you want to do\n> ")

    if choice_4c == "1":
        Enter_cave()
    elif choice_4c == "2":
        print("You see a nice green forest below")
        x = input("Would you like to rest here,  (y or n)\n> ")
        if x == "y":
            sit()
        elif x == "n":
            Enter_cave()
        else:
            print("Invalid choice, Try again")
    elif choice_4c == "3":
        Jump()
    else:
        print("Invalid choice, Try again")
        Walk_around()
# Shop Path
def leave_1():
    print("You leave the shop with a rusty sword")
    print("You now enter the forest and with your new sword and the map the villager gave you")
    print("you come to a fork in the do you want to go (right) or (left)")

    choice_4d = input("What would you like to do\n> ")

    if choice_4d == "right":
        right()
    elif choice_4d == "left":
        walk_away_2()
    else:
        print("Invalid choice, Try again")
        leave_1()

def leave_2():
    print("You leave the shop with a rusty rusty set of armor")
    print("You now enter the forest and with your new set of gear and the map the villager gave you")
    print("you come to a fork in the do you want to go (right) or (left)")

    choice_4d = input("What would you like to do\n> ")

    if choice_4d == "right":
        right_2()
    elif choice_4d == "left":
        walk_away_3()
    else:
        print("Invalid choice, Try again")
        leave_2()

def leave_3():
    print("You leave the shop with a heal pot")
    print("You now enter the forest and with your heal pot and the map the villager gave you")
    print("you come to a fork in the do you want to go (right) or (left)")

    choice_4d = input("What would you like to do\n> ")

    if choice_4d == "right":
        right_3()
    elif choice_4d == "left":
        walk_away_4()
    else:
        print("Invalid choice, Try again")
        leave_3()

def leave_4():
    print("You leave the shop would you like to")
    print("1. re-enter the shop")
    print("2. enter the forest")
    
    choice_44 = input("What would you like to do\n>")
    
    if choice_44 == "1":
        shop()
    elif choice_44 == "2":
        enter_forest()
    else:
        print("Invalid choice, Try again")
        leave_4()
# Part 3d
def search():
    print("You end up looking around for a wepon and you happen apon a pointy stick")
    print("You pick up the stick and you look at the monsters that now see you")
    print("do you want to")
    print("1. fight")
    print("2. Clime a tree")
    print("3. Drop it and Run")
    print("4. let them take your life you give up")

    choice_4e = input("What do you want to do\n> ")

    if choice_4e == "1":
        Charge()
    elif choice_4e == "2":
        Tree()
    elif choice_4e == "3":
        walk_away()
    elif choice_4e == "4":
        ending_1()
    else:
        print("Invalid choice, Try again")
        search()

def enter_deeper():
    print("As you start to enter the cave the ground shakes and the only way in behind you colapses.")
    print("You are now traped and the only opptions forward ")
    print("finaly you come to a inter section in the cave ")
    print("would you like to head ")
    print("1. Left")
    print("2. Right")
    print("3. straight")
    print("4. stay put")

    choice_4f = input("What would you like to do\n> ")

    if choice_4f == "1":
        cave_left()
    elif choice_4f == "2":
        cave_right()
    elif choice_4f == "3":
        head_forward()
    elif choice_4f == "4":
        stay_put()
    else:
        print("Invalid choice. Try again")
        enter_deeper()

def Leave_cave():
    print("You leave the cave and all the sudding the ground starts shaking and the cave entrence behind you colapses.")
    print("with no other way to got you head back")
    print("back the other way")
    back_at_the_nest()

def sit():
    print("You take seat in a near by rock and look out over the cliff")
    print("As you about to get up you hear a voice speak to you across the fog")
    print("Do you")
    print("1. Talk with it")
    print("2. Walk away")
    print("3. Jump")
    print("4. Wait")

    choice_sit = input("What would you do\n> ")

    if choice_sit == "1":
        Talk()
    elif choice_sit == "2":
        walk_away_cliff()
    elif choice_sit == "3":
        Jump()
    elif choice_sit == "4":
        Wait()
    else:
        print("Invalid choice, Try again")
        sit()
    
def Jump():
    print("You decied to jump off")
    print("As you fall you start to think how is the dummy that is making the choices")
    print("As you finish your tought you hit the ground flat as a pancake and with no one or nothing to help you you die")
    ending_1()

def Wait():
    print("Ok I can wait")
    stay = input("type ready when you want to move on\n> ")

    if stay == "ready":
        sit()
    else:
        print("Invalid choice. Try again")
        Wait()

# Shop path right
def right():
    print("you enter the forest and head to the right. as you wander deeper into the outer layer you happen across a monsters nest. What do you do.")
    print("1. Take a stealthy aproche.")
    print("2. Charge in with your sword.")
    print("3. Stand there till they notice you.")
        
    choice_2a = input("What would you do\n> ")
    
    if choice_2a == "1":
        stealth_1a()
    elif choice_2a == "2":
        attack_with_sword()
    elif choice_2a == "3":
        stay()
    else:
        print("Invalid choice. Try again")
        right() 

def right_2():
    print("you enter the forest and head to the right. as you wander deeper into the outer layer you happen across a monsters nest. What do you do.")
    print("1. take a stealthy aproche.")
    print("2. You got armor walk in like a chad and fist fight.")
    print("3. Search There Area")
        
    choice_2a = input("What would you do\n> ")
    
    if choice_2a == "1":
        stealth_1b()
    elif choice_2a == "2":
        Chad()
    elif choice_2a == "3":
        search_ab()
    else:
        print("Invalid choice. Try again")
        right_2()

def right_3():
    print("you enter the forest and head to the right. as you wander deeper into the outer layer you happen across a monsters nest. What do you do.")
    print("1. take a stealthy aproche and fight.")
    print("2. walk away.")
    print("3. Stand there till they notice you.")
        
    choice_2a = input("What would you do\n> ")
    
    if choice_2a == "1":
        stealth_1c()
    elif choice_2a == "2":
        walk_away_3()
    elif choice_2a == "3":
        stay()
    else:
        print("Invalid choice. Try again")
        right_3()

# Shop path away(left)
def walk_away_2():
    print("you decied to head to the left untill you happen apon a cave.")
    print("What do you want to do")
    print("1. Enter the cave.")
    print("2. walk around the cave")
    print("3. Head right")
    print("4. Your to sacred to fight at all and call it quits")
    
    choice_3b = input("What would you do\n> ")
    
    if choice_3b == "1":
        Enter_cave_2()
    elif choice_3b == "2":
        Walk_around_2()
    elif choice_3b == "3":
        right()
    elif choice_3b == "4":
        ending_2()
    else:
        print("Invalid choice. Try again")
        walk_away_2()

def walk_away_3():
    print("you decied to head to the left untill you happen apon a cave.")
    print("What do you want to do")
    print("1. Enter the cave.")
    print("2. walk around the cave")
    print("3. Head to the right")
    print("4. Your to sacred to fight at all and call it quits")
    
    choice_3b = input("What would you do\n> ")
    
    if choice_3b == "1":
        Enter_cave_3()
    elif choice_3b == "2":
        Walk_around_3()
    elif choice_3b == "3":
        right_2()
    elif choice_3b == "4":
        ending_2()
    else:
        print("Invalid choice. Try again")
        walk_away_3()

def walk_away_4():
    print("you decied to head to the left untill you happen apon a cave.")
    print("What do you want to do")
    print("1. Enter the cave.")
    print("2. walk around the cave")
    print("3. Head to the right")
    print("4. Your to sacred to fight at all and call it quits")
    
    choice_3b = input("What would you do\n> ")
    
    if choice_3b == "1":
        Enter_cave_4()
    elif choice_3b == "2":
        Walk_around_4()
    elif choice_3b == "3":
        right_3()
    elif choice_3b == "4":
        ending_2()
    else:
        print("Invalid choice. Try again")
        walk_away_4()

# Search path
def Charge():
    print("You charge forwars with your stick in hand")
    print("You make contact and pierce one. When you got to remove the stick you find that it is stuck in the monsters chest ")
    print("You don't have much time befor the second one gets to you")
    print("")
    print("COMPLET THE MAZE TO REMOVE THE STICK USE W FOR UP, D FOR RIGHT, A FOR LEFT, S FOR DOWN")
    print("MOVEING WILL BRING YOU TO THE NEXT INTERSECTION OR WALL")
    print("")
    print("_______Start Here________")
    print("|_________ YOU ______ __|")
    print("|  ___________  ___|____|")
    print("|  _______|_______ _____|")
    print("|_____  ___ ___|______ _|")
    print("|  _____|      |_____  _|")
    print("|  ___ _|___|__|____    |")
    print("|_|_____|_  x |__  _____|")
    print("|_______________________|")
    
    print("END AT X")
    print("")
    maze = input("ENTER THE RIGHT PATH WITH NO SPACES AND ALL CAPS FIRST TRY\n> ")

    if maze == "SDSDSDSSASAW":
        Kill()
    else :
        ending_1()

def Tree():
    print("You now find youself up in a tree with two monsters below to wanting to leave till you die") 
    print("What do you do")
    print("1. Jump em")
    print("2. Wait")
    print("3. Throw your stick at them")
    print("4. Try and make a break for it")

    choice_tree = input("What would you do\n> ")

    if choice_tree == "1":
        Jump_em()
    elif choice_tree == "2":
        Wait()
    elif choice_tree == "3":
        Throw()
    elif choice_tree == "4":
        ending_1()
    else:
        print("Invalid choice. Try again")
        Tree()

def cave_left():
    print("You head on to the left ")
    print("and you find your self standing infront of masive masive monster")
    print("you try to leave but befor you can get out hit picks up a bolder and uses it to block the entrence ")
    print("You now are forced to fight")

    come_back_to

def cave_right():
    print("you walk untill you find your self at a dead end ")
    print("would you like to")
    print("1. Head back")
    print("2. Stay put")

    cave_right_a = input("What would you like to do\n> ")

    if cave_right_a == "1":
        enter_deeper()
    elif cave_right_a == "2":
        stay_put()
    else:
        print("Invalid choice. Try again")
        cave_right()

def head_forward():
    print("you walk untill you find your self at a dead end ")
    print("would you like to")
    print("1. Head back")
    print("2. Stay put")

    cave_right_a = input("What would you like to do\n> ")

    if cave_right_a == "1":
        enter_deeper()
    elif cave_right_a == "2":
        stay_put()
    else:
        print("Invalid choice. Try again")
        head_forward()

def stay_put():
    print("Ok I can wait")
    stay = input("type ready when you want to move on\n> ")

    if stay == "ready":
        cave_right()
    else:
        print("Invalid choice. Try again")
        stay_put()

def back_at_the_nest():
    print("back at the nest you take another look at the mosters. You can")
    print("1. take a stealthy aproche.")
    print("2. walk away.")
    print("3. Stand there till they notice you.")
        
    choice_2a = input("What would you do\n> ")
    
    if choice_2a == "1":
        stealth()
    elif choice_2a == "2":
        walk_away()
    elif choice_2a == "3":
        stay()
    else:
        print("Invalid choice. Try again")
        back_at_the_nest()

def Talk():
    print("You decide to talk and here what the voice has to say")
    print("The voice tells you it can grant you great power in return you slay the beast in the cave")
    
    talk = input("Do you wish to except (y or n)")

    if talk == "y":
        enter_cave_with_power()
    elif talk == "n":
        print("VOICE -  Very well")
        walk_away_cliff()
    else:
        print("Invalid choice. Try again")
        Talk()

def walk_away_cliff():
    print("You head back to the front of the cave")
    print("Do you wish to")
    print("1. enter cave")
    print("2. head back to the nest")

    Walk_away_cliff = input("What would you like to do\n> ")

    if Walk_away_cliff == "1":
        Enter_cave()
    elif Walk_away_cliff == "2":
        back_at_the_nest()

def stealth_1a():
    print("You choice to sneak up on the two monsters ")
    print("You can")
    print("1. draw your sword ")
    print("2. sneak buy")
    print("3. search")

    Stealth_1a = input("What would you like to do\n> ")

    if Stealth_1a == "1":
        attack_with_sword()
    elif Stealth_1a == "2":
        Sneak_by()
    elif Stealth_1a == "3":
        search_b()
    else:
        print("Invalid choice. Try again")
        stealth_1a()

def search_b():
    print("All you find is some pointy sticks and you better off with your sword")
    print("Would you like to")
    print("1. draw your sword ")
    print("2. sneak buy")

    Stealth_1B = input("What would you like to do\n> ")

    if Stealth_1B == "1":
        attack_with_sword()
    elif Stealth_1B == "2":
        Sneak_by()
    else:
        print("Invalid choice. Try again")
        search_b()

def attack_with_sword():
    print("You sneak up ready to attack with your sword in hand")
    print("COMPLET THE MAZE TO KILL YOUR ENEIMY. USE W FOR UP, D FOR RIGHT, A FOR LEFT, S FOR DOWN")
    print("MOVEING WILL BRING YOU TO THE NEXT INTERSECTION OR WALL")
    print("FAILER WILL RESULT IN YOUR DEATH")
    print("")
    print("_______Start Here________")
    print("|_________ YOU ______ __|")
    print("|  ___________  ___|____|")
    print("|  _______|_______ _____|")
    print("|_____  ___ ___|______ _|")
    print("|  _____|      |_____  _|")
    print("|  ___ _|___|__|____    |")
    print("|_|_____|_  x |__  _____|")
    print("|_______________________|")
    
    print("END AT X")
    print("")
    maze = input("ENTER THE RIGHT PATH WITH NO SPACES AND ALL CAPS FIRST TRY\n> ")

    if maze == "SDSDSDSSASAW":
        kill_sword()
    else:
        print("You failed")
        ending_1()

def stealth_1b():
    print("You choice to sneak up on the two monsters ")
    print("You can")
    print("1. fist fight ")
    print("2. sneak buy")
    print("3. search")

    Stealth_1ab = input("What would you like to do\n> ")

    if Stealth_1ab == "1":
        attack_with_fist_and_armor()
    elif Stealth_1ab == "2":
        Sneak_by()
    elif Stealth_1ab == "3":
        search_ab()
    else:
        print("Invalid choice. Try again")
        stealth_1b()

def attack_with_fist_and_armor():
    print("You attak with your fist along with your armor to take out the monsters")
    print("COMPLET THE MAZE TO KILL YOUR ENEIMY. USE W FOR UP, D FOR RIGHT, A FOR LEFT, S FOR DOWN")
    print("MOVEING WILL BRING YOU TO THE NEXT INTERSECTION OR WALL")
    print("FAILER WILL RESULT IN YOUR DEATH")
    print("")
    print("_______Start Here________")
    print("|_________ YOU ______ __|")
    print("|  ___________  ___|____|")
    print("|  _______|_______ _____|")
    print("|_____  ___ ___|______ _|")
    print("|  _____|      |_____  _|")
    print("|  ___ _|___|__|____    |")
    print("|_|_____|_  x |__  _____|")
    print("|_______________________|")
    
    print("END AT X")
    print("")
    maze = input("ENTER THE RIGHT PATH WITH NO SPACES AND ALL CAPS FIRST TRY\n> ")

    if maze == "SDSDSDSSASAW":
        kill_armor()
    else:
        print("You faild")
        ending_1()

def search_ab():
    print("You search the area and find a stick you can use to help")
    print("Would you like to")
    print("1. Fight")
    print("2. Sneak by")

    choice_ab = input("what would you like to do\n> ")

    if choice_ab == "1":
        aromr_stick()
    elif choice_ab == "2":
        Sneak_by()
    else:
        print("Invalid choice. Try again")
        search_ab()

def Chad():
    print("You stand there and slowly start walking towrd your enemy")
    attack_with_fist_and_armor()

def stealth_1c():
    print("You attak with your fist to take out the monsters")
    print("COMPLET THE MAZE TO KILL YOUR ENEIMY. USE W FOR UP, D FOR RIGHT, A FOR LEFT, S FOR DOWN")
    print("MOVEING WILL BRING YOU TO THE NEXT INTERSECTION OR WALL")
    print("FAILER WILL RESULT IN YOUR DEATH (except you have heal potions)")
    print("")
    print("_______Start Here________")
    print("|_________ YOU ______ __|")
    print("|  ___________  ___|____|")
    print("|  _______|_______ _____|")
    print("|_____  ___ ___|______ _|")
    print("|  _____|      |_____  _|")
    print("|  ___ _|___|__|____    |")
    print("|_|_____|_  x |__  _____|")
    print("|_______________________|")
    
    print("END AT X")
    print("")
    maze = input("ENTER THE RIGHT PATH WITH NO SPACES AND ALL CAPS FIRST TRY\n> ")

    if maze == "SDSDSDSSASAW":
        kill_potion()
    else:
        print("Invalid choice. You take a sip of your heal potion try again.")
        stealth_1c()

def Enter_cave_2():
    print("You deiced to enter the near by cave")
    print("Do you want to.")
    print("1. Enter in further")
    print("2. Look around")

    choice_4b = input("What do you want to do\n> ")

    if choice_4b == "1":
        enter_deeper_2()
    elif choice_4b == "2":
        print("")
        print("like the view")
        print("")
        Enter_cave_2()
    else:
        print("Invalid choice, Try again")
        Enter_cave_2()

def Enter_cave_3():
    print("You deiced to enter the near by cave")
    print("Do you want to.")
    print("1. Enter in further")
    print("2. Look around")

    choice_4b = input("What do you want to do\n> ")

    if choice_4b == "1":
        enter_deeper_3()
    elif choice_4b == "2":
        print("")
        print("like the view")
        print("")
        Enter_cave_3()
    else:
        print("Invalid choice, Try again")
        Enter_cave_3()

def Enter_cave_4():
    print("You deiced to enter the near by cave")
    print("Do you want to.")
    print("1. Enter in further")
    print("2. Look around")

    choice_4b = input("What do you want to do\n> ")

    if choice_4b == "1":
        enter_deeper_4()
    elif choice_4b == "2":
        print("")
        print("like the view")
        print("")
        Enter_cave_4()
    else:
        print("Invalid choice, Try again")
        Enter_cave_4()

def Walk_around_2():
    print("You finaly make it around the cave and find your self at the edge of a cliff.")
    print("Do you want to")
    print("1. Turn back and enter cave")
    print("2. Look around")
    print("3. Jump")

    choice_4c = input("What do you want to do\n> ")

    if choice_4c == "1":
        Enter_cave_2()
    elif choice_4c == "2":
        print("You see a nice green forest below")
        x = input("Would you like to rest here ,  (y or n)\n> ")
        if x == "y":
            sit_2()
        elif x == "n":
            Enter_cave_2()
        else:
            print("Invalid choice, Try again")
    elif choice_4c == "3":
        Jump()
    else:
        print("Invalid choice, Try again")
        Walk_around()

def sit_2():
    print("You take a seat on a rock and look at the great forest below")
    stay = input("type ready when you want to move on and head into the cave\n> ")

    if stay == "ready":
        Enter_cave_2()
    else:
        print("Invalid choice. Try again")
        sit_2()

def Walk_around_3():
    print("You finaly make it around the cave and find your self at the edge of a cliff.")
    print("Do you want to")
    print("1. Turn back and enter cave")
    print("2. Look around")
    print("3. Jump")

    choice_4c = input("What do you want to do\n> ")

    if choice_4c == "1":
        Enter_cave_3()
    elif choice_4c == "2":
        print("You see a nice green forest below")
        x = input("Would you like to rest here ,  (y or n)\n> ")
        if x == "y":
            sit_3()
        elif x == "n":
            Enter_cave_3()
        else:
            print("Invalid choice, Try again")
    elif choice_4c == "3":
        Jump()
    else:
        print("Invalid choice, Try again")
        Walk_around()

def sit_3():
    print("You take a seat on a rock and look at the great forest below")
    stay = input("type ready when you want to move on and head into the cave\n> ")

    if stay == "ready":
        Enter_cave_3()
    else:
        print("Invalid choice. Try again")
        sit_3()

def Walk_around_4():
    print("You finaly make it around the cave and find your self at the edge of a cliff.")
    print("Do you want to")
    print("1. Turn back and enter cave")
    print("2. Look around")
    print("3. Jump")

    choice_4c = input("What do you want to do\n> ")

    if choice_4c == "1":
        Enter_cave_4()
    elif choice_4c == "2":
        print("You see a nice green forest below")
        x = input("Would you like to rest here ,  (y or n)\n> ")
        if x == "y":
            sit_4()
        elif x == "n":
            Enter_cave_4()
        else:
            print("Invalid choice, Try again")
    elif choice_4c == "3":
        Jump_b()
    else:
        print("Invalid choice, Try again")
        Walk_around()

def sit_4():
    print("You take a seat on a rock and look at the great forest below")
    stay = input("type ready when you want to move on and head into the cave\n> ")

    if stay == "ready":
        Enter_cave_4()
    else:
        print("Invalid choice. Try again")
        sit_4()

def Jump_b():
    print("You jump and hit the ground so hard your seconds from death but with you last breathing moments you sip down some of you heal potion ")
    print("When you regain your strgenth you look around and relise there is no way back up the cliff and you have no idea were your at")
    ending_3()


start_adventure()



