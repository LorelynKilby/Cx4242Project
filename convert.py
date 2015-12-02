import csv
import json
from pprint import * 

csvfile = open('policies.csv')

l = []
i = 1
for row in csvfile:
    r= row.split(",")
    newrow = {"id": i, "type": 'point', 'content': r[1] , 'start': r[0]}
    l.append(newrow)
    i += 1

print l

