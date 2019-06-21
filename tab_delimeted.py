import csv

with open("tab_delimeted.txt", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])

        # process(date, symbol, closing_price)

        # print(date)