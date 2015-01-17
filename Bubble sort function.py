#Nicola Batty
#13/01/2015
#Bubble sort function

def input_list():
    number = int(input("How many in list: "))
    list1 = []
    for count in range(number):
        itam = input("plese enter an itam on the list: ")
        list1.append(itam)
    return list1, number

def sort_list(list1, number):
    #pdb.set_trace()
    swaps = False
    while not swaps:
        swaps = True
        count = 0
        for itam in list1:
            if count < number - 1:
                if itam > list1[count+1]:
                    swaps = False
                    temp = itam
                    list1[count] = list1[count+1]
                    list1[count+1] = temp
                count = count + 1
    return list1

def output_sorted_list(list1):
    for itam in list1:
        print(itam)

def sort():
    list1, number = input_list()
    list1 = sort_list(list1, number)
    output_sorted_list(list1)
