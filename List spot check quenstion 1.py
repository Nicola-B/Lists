#Nicola Batty
#27/01/2015
#List spot check quenstion 1

scores = [18, 23, 36, 21, 58, 40, 45, 59]
number = 8
for count1 in range(number-1):
    for count2 in range(number-1):
        if scores[count2] > scores[count2 + 1]:
            temp = scores[count2]
            scores[count2] = scores[count2 + 1]
            scores[count2 + 1] = temp

number1 = 1

for index in range(number):
    print("{0}) {1}".format(number1, scores[index]))
    number1 = number1+1
