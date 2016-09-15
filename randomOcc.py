#Emma and Shaeq
#SoftDev pd 6
#Mr. DW
#09.15.16

import random
import csv

def readToDict():
    with open('occupation.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row.split(',')
        occs[row[0]] = row[1]
