import pandas as pd
import numpy as np
import csv
from pprint import *

f = open("population.csv",'rt')
reader = csv.reader(f)

predictions = []
years = range(1964,2014)
regression_records = [['State','coef','intercept']]

for row in reader:
    newrow = [row[0]]
    regression_record = [row[0]]
    values = []
    print row
    for i in range(1,51):

        print i
        values.append(float(row[i]))

    d = { 'year' : years ,
            'values' : values}
    rowData = pd.DataFrame(d)
    x = rowData['year']
    y = rowData['values']

    regression = np.polyfit(x, y, 1)
    regression_record.extend(regression)

    regression_records.append(regression_record)

    for yr in range(2014,2021):
        yv = regression[0]*yr + regression[1]
        newrow.append(yv)

    predictions.append(newrow)


pprint(predictions)

with open("Predictions-Populations.csv",'wb') as f:
    writer = csv.writer(f)
    writer.writerows(predictions)

with open("RegressionRecords-Population.csv",'wb') as of:
    writer = csv.writer(of)
    writer.writerows(regression_records)