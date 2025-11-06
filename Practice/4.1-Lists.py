# Creathing a simple list
'''
fav_fruits.append("pear")    - Adds index to end of list
fav_fruits.insert(1, "cherry")  - Adds index at position
fav_fruits.extend(fav_candy)  - Adds list to end of list

fav_fruits.remove("bannana") - Removes first occurance of value
fav_fruits.pop(1) - Removes specific indexs
fav_fruits.clear() - Removes every item in the list

fav_fruit.sort()  - Sorts list
print(fav_fruits.index("apple")) - Tells me it's place 
print(len(fav_fruits)) - Tells me number of iteams in the list
print(max(numbers))
print(min(numbers))

'''
def remove_fruit():
    fav_fruits = ["orange's","apples", "mangos" ,"bannana", "pear's"]


    print(fav_fruits[0]) 
    print(fav_fruits[4])
    fav_fruits.append("cherry")
    print(fav_fruits)

    remove = input("What fruit would you like to remove from the list\n> ")

    if remove == "orange's":
        fav_fruits.pop(0)
        print(fav_fruits)
    elif remove == "apples":
        fav_fruits.pop(1)
        print(fav_fruits)
    elif remove == "mangos":
        fav_fruits.pop(2)
        print(fav_fruits)
    elif remove == "bannana":
        fav_fruits.pop(3)
        print(fav_fruits)
    elif remove == "pear's":
        fav_fruits.pop(4)
        print(fav_fruits)
    else:
        print("Invalid input")
        remove_fruit()

remove_fruit()