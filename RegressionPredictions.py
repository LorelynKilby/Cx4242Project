import pandas as pd
import numpy as np
import csv
from pprint import *

f = open("cleaneddata.csv",'rt')
reader = csv.reader(f)

predictions = []
startyear = 2000
endyear = 2010

dif = endyear-startyear
st = startyear- 1960 + 2

years = range(startyear,endyear)

predictyears = range(endyear,endyear+10)
print predictyears

regression_records = [['State','Source','coef','intercept']]

for row in reader:
    newrow = [row[0],row[1] ]
    regression_record = [row[0],row[1]]
    values = []

    for i in range(st,st+dif):
        values.append(float(row[i]))

    d = { 'year' : years ,
            'values' : values}
    rowData = pd.DataFrame(d)
    x = rowData['year']
    y = rowData['values']

    regression = np.polyfit(x, y, 1)
    regression_record.extend(regression)

    regression_records.append(regression_record)

    for yr in predictyears:
        yv = regression[0]*yr + regression[1]
        newrow.append(yv)

    predictions.append(newrow)


pprint(predictions)

measure = str(endyear) + "-" + str((endyear+10))

f1 = "predictions-Energy-" + measure + ".csv"
f2 = "regressionRecords-Energy-" + measure + ".csv"

with open(f1,'wb') as f:
    writer = csv.writer(f)
    writer.writerows(predictions)

with open(f2,'wb') as of:
    writer = csv.writer(of)
    writer.writerows(regression_records)