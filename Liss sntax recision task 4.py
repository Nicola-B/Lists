#Nicola Batty
#06/01/2015
#Liss sntax recision task 4

def print_pet (pets):
    for pet in pets:
        print(pet)

def print_number (pets):
    for index, pet in enumerate(pets):
        print("{0}.{1}".format(index+1,pet))

#main programe
pets = ["dog", "cat", "goldfish", "hamster", "rabbit", "gerbil"]
print_pet(pets)
print_number(pets)
