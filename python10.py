import csv
rows = [
    (2, 'Bình', 25),
    (3, 'Thư', 24)
]
with open('demo.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow([1, 'An', 20])
    csv.writer(f).writerows(rows)
with open('demo.csv','r',encoding='utf-8') as f:
    read = csv.DictReader(f)
    for row in read:
        print(row)