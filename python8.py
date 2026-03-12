from csv import *
with open('annual-enterprise-survey-2024-financial-year-provisional.csv', mode='r',encoding='utf-8',errors='ignore') as f:
    reader = DictReader(f)
    for row in reader:
        value = row.get('Value')
        if not value:
            value = 0
            continue
        if len(value) < 1:
            print('Không có giá trị, dòng rỗng')
            continue
        print(value)

with open('demo.csv',mode='r',encoding='utf-8') as f:
    for row in DictReader(f):
        if not row.strip():
            continue
        amount = int(row['name'])
        print(amount)