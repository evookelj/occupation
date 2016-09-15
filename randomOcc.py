#Emma and Shaeq
#SoftDev pd 6
#Mr. DW
#09.15.16

from random import choice
import csv

occs = {}

def readToDict():
    import csv
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row['Job Class']
            percent = float(row['Percentage'])
            if (job != 'Total'): occs[job] = percent

def pickWeighted():
    print choice([occs[k] for k in occs])

def getRandOccupation():
    readToDict()
    pickWeighted()

getRandOccupation()
