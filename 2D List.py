#Nicola Batty
#06/01/2015
#2D List

def table(table):
    for row in table:
        print("|{0:<12}|{1:<4}|{2:<6}|".format(row[0], row[1], row[2]))

players = [
    ["name", "kill", "deaths"],
    ["k1llnAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]
]

table(players)
