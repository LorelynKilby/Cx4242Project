import csv
import json
from pprint import * 

f = open("cleaneddata.csv",'rt')
reader = csv.reader(f)

predictions = [['State','Soruce','2014','2015','2016','2017','2018','2019','2020']]
years = range(1960,2014)
print years

for row in reader:
    newrow = [row[0],row[1] ]


l = []
i = 1
for row in csvfile:
    r= row.split(",")
    print r 
    newrow = {'id': i, 'content': r[1] , 'start': r[0]}
    l.append(newrow)
    i += 1

print l

