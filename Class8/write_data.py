import csv
filename = 'SanJose_weather.csv'
with open(filename) as wdata:
    reader=csv.reader(wdata)
    header_row=next(reader)
    print(header_row)