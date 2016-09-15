#Emma V, Shaeq A, Jason C
#SoftDev pd 6
#Mr. DW
#09.15.16

from random import choice, uniform
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
    rand = uniform(0, sum(occs.itervalues())) #rand float from 0 to sum of vals
    sigma = 0.0
    for key, weight in occs.iteritems():
        sigma += weight
        if rand < sigma: return key;
    return key

def getRandOccupation():
    readToDict()
    return pickWeighted()

print getRandOccupation()
