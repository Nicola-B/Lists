#Nicola Batty
#06/01/2015
#2D List table function

def table(table1):
    print("-"*27)
    count = 0
    for row in enumerate(table1):
        print("|{0:<12}|{1:<5}|{2:<7}|".format(table1[count][0], table1[count][1], table1[count][2]))
        print("-"*27)
        count = count+1
        
#main program
table1 = [
    ["name", "kill", "deaths"],
    ["k1llnAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]
    ]
table(table1)
