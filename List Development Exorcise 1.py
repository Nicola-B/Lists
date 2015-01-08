#Nicola Batty
#08/01/2015
#List Development Exorcise 1

import random

def random_genorater():
    random_num = random.randint(0, 9)
    return random_num

def lists():
    country = [
        ["England", "Loundon"],
        ["Norway", "Oslo"],
        ["USA", "Washington, D.C."],
        ["Brazil", "Brasilia"],
        ["Russia", "Moscow"],
        ["Autralia", "Canberra"],
        ["Canada", "Ottawa"],
        ["Chile", "Santiago"],
        ["Peru", "Lima"],
        ["Portugal", "Lisbon"]
        ]
    return country

def question(country):
    random_num = random_genorater()
    country1 = country[random_num][0]
    right_anwser = country[random_num][0]
    anwser = input("What is the capitale city of {0}: ".format(country1))
    return anwser, random_num

def display_wrong_or_right(wrong_right, right_anwser):
    if wrong_right == "true":
        print("Correct")
    else:
        print("Wrong, the anwser is {0}.".format(right_anwser))

def countries():
    country = lists()
    anwser, random_num = question(country)
    right_anwser = country[random_num][1]
    if anwser == right_anwser:
        wrong_right = "true"
    else:
        wrong_right = "fulse"
    display_wrong_or_right(wrong_right, right_anwser)
