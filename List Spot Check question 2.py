#Nicola Batty
#27/01/2015
#List Spot Check question 2

import random

def generate_random_number():
    number = random.randint(1, 6)
    return number

def record_score_in_list(scroes, number):
    number = number - 1
    temp = scroes[number]
    temp = temp + 1
    scroes[number] = temp
    return scroes

def initialise_frequency_list():
    scroes = []
    for count in range(0, 6):
        scroes.append(0)
    return scroes

def simulate_die_throwing(scroes):
    for count in range(0, 20):
        number = generate_random_number()
        scroes = record_score_in_list(scroes, number)
    return scroes

def display_result_list(scroes):
    print("_"*7)
    for count in range(0, 6):
        print("|{0:<2}|{1:<2}|".format(count + 1, scroes[count]))
        print("_"*7)

def frequency_of_die_scores():
    scroes = initialise_frequency_list()
    scroes = simulate_die_throwing(scroes)
    display_result_list(scroes)
