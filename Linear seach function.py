#Nicola Batty
#09/01/2015
#Linear seach function

#import pdb

def output_message(message):
    print(message)

def input_list():
    number = int(input("How many in list: "))
    list1 = []
    for count in range(number):
        print(count)
        itam = ("plese enter an itam on the list: ")
        list1.append(itam) 
    return list1, number

def input_itam():
    itam = input("Please input an itam: ")
    return itam

def input_massage():
    massage1 = input("plese input the message shown if the itam is found:")
    massage2 = input("plese input the massage shown if the itam is not found:")
    return massage1, massage2
def linear_sarch(search_list, search_itam, message1, number):
    found = False
    count = 0
    while not found and count < number:
        if search_list[count] == search_itam:
            output_message(message1)
            found = True
    return found

def main():
    #pdb.set_trace()
    list1, number = input_list()
    itam = input_itam()
    massage1, massage2 = input_massage()
    found = linear_sarch(list1, itam, massage1, number)
    if not found:
        output_message(message2)
    
