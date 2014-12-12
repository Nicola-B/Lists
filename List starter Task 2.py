#Nicola Batty
#12/12/2014
#List starter Task 1

shopping_list = []
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

for index, shopping_item in enumerate(shopping_list):
	print("Item {0} is {1}".format(index+1, shopping_item))
