import pandas as pd
import numpy as np
import csv
from pprint import *

f = open("cleaneddata.csv",'rt')
reader = csv.reader(f)

predictions = []
years = range(1960,2000)
regression_records = [['State','Source','coef','intercept']]

for row in reader:
    newrow = [row[0],row[1] ]
    regression_record = [row[0],row[1]]
    values = []

    for i in range(2,42):
        values.append(float(row[i]))

    d = { 'year' : years ,
            'values' : values}
    rowData = pd.DataFrame(d)
    x = rowData['year']
    y = rowData['values']

    regression = np.polyfit(x, y, 1)
    regression_record.extend(regression)

    regression_records.append(regression_record)

    for yr in range(2000,2010):
        yv = regression[0]*yr + regression[1]
        newrow.append(yv)

    predictions.append(newrow)


pprint(predictions)

with open("predictions-Energy-2000-2010.csv",'wb') as f:
    writer = csv.writer(f)
    writer.writerows(predictions)

with open("regressionRecords-Energy-2000-2010.csv",'wb') as of:
    writer = csv.writer(of)
    writer.writerows(regression_records)