#Emma and Shaeq
#SoftDev pd 6
#Mr. DW
#09.15.16

import random
import csv

occs = {}

def readToDict():
    import csv
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row['Job Class']
            if (job != 'Total'):
                occs[job] = row['Percentage']             
                print job + ": " + occs[job]

readToDict()
