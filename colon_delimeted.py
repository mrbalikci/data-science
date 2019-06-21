import csv

with open("colon_delimeted.txt", "r") as f:
    reader = csv.DictReader(f, delimiter=':')

    for row in reader:
        date = row['date']
        symbol = row['symbol']
        closing_price = float(row['closing_price'])

        process(date,symbol,closing_price)