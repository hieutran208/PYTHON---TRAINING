import csv
from datetime import datetime
rows = [
    ('2024-12-8',8340000),
    ('2024-12-31',120000)
]
with open('demo.csv',mode='a',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
with open('demo.csv',mode='r',encoding='utf-8') as f:
    for row in csv.DictReader(f,delimiter=';'):
        row['amount'] = int(row['amount'].replace(',',''))
        row['date'] = datetime.strptime(row['date'],'%Y-%m-%d')
        print(row)