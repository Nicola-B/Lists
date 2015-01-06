#Nicola Batty
#06/01/2015
#2D List table function

def table(table):
    for row in enumerate(table):
        print("|{0}|{1}|{2}|".format(row[0], row[1], row[2]))
