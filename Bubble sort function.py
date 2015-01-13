#Nicola Batty
#13/01/2015
#Bubble sort function

import pdb

def input_list():
    number = int(input("How many in list: "))
    list1 = []
    for count in range(number):
        itam = input("plese enter an itam on the list: ")
        list1.append(itam) 
    return list1

def sort_list(list1):
    count = 0
    swaps = false
while not swaps: 
    for itam in list1:
        if itam > list1[count+1]:
            temp = itam
            list1[count] = list1[count+1]
            list1[count+1] = temp
        count = count + 1
    return list1

def output_sorted_list(list1):
    for itam in list1:
        print(itam)

def sort():
    pdb.set_trace()
    #list1 = input_list()
    list1 = [10, 7, 3, 12, 1, 500, 90]
    list1 = sort_list(list1)
    output_sorted_list(list1)
