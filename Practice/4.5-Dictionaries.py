'''
tyler_faves = {
    "Video Game": "Elden Ring",
    "Food": "Bacon",
    "Color": "Black",
    "Age": "17",
    "Class": "Intro to Programming"

}

print(tyler_faves["Food"])

# Add a new entry
tyler_faves["pokemon"] = "Hawlucha"

# Modify an entry
tyler_faves["Color"] = "Red"

# Remove an entry
tyler_faves.pop("Class")

#Looping through a dictionary
for key, value in tyler_faves.items():
    print(key + ": " + str(value))

print(tyler_faves.keys())
print(tyler_faves.values())
print(tyler_faves.items())
tyler_faves.clear()
print(tyler_faves)
'''

studients_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "B",
    "Eve": "F"
}

student = {
    "name": "Alice",
    "age": 16, 
    "grade": "A"
}

print(str(student["name"]) + ": " + str(student["age"]))

