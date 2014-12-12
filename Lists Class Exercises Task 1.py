#Nicola Batty
#12/12/2014
#Program to search for a name in a list
#Lists Class Exercises Task 1
NamesList = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

ElementSought = input('Enter the name you are searching for : ')
ThisElement = 0
Found = False
while not Found:
       if NamesList[ThisElement] == ElementSought:
          Found = True
          print('{0} was in element {1} in the list'.format(ElementSought, ThisElement))
       else:
          ThisElement = ThisElement + 1
          if ThisElement == 5:
              print('Not found')
              Found = True
