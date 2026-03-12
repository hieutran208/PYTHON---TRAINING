import csv
users = [
    {'id': 1, 'name': 'An', 'age': 20},
    {'id': 2, 'name': 'Bình', 'age': 22}
]
with open('data.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=users[0].keys(),delimiter=';')
    writer.writeheader()
    writer.writerows(users)
with open('data.csv', 'a', encoding='utf-8', newline='') as f:
    header = ['id', 'name', 'age']
    writer = csv.DictWriter(f, fieldnames=header,delimiter='|')
    writer.writeheader()
    writer.writerow({'id': 1, 'name': 'An', 'age': 20}) # Viết writer.writerow(['1', 'An', '20']) => lỗi
with open('data.csv','r',encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)