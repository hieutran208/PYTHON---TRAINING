from datetime import *
name = 'Hiếu'
age = 25 
with open('C:/Users/USER/OneDrive/Desktop/GSAT.txt',mode='w',encoding='utf-8') as f:
    f.write(f'Tên: {name}\n')
    f.write(f'Tuổi: {age}\n')

with open('C:/Users/USER/OneDrive/Desktop/GSAT.txt', 'a', encoding='utf-8') as f:
    f.write(f'{datetime.now()}|ERROR|amount > balance\n')

data = [
    ('20250205', 'SUCCESS', 1000),
    ('20250205', 'ERROR', 5000)
]
with open('C:/Users/USER/OneDrive/Desktop/GSAT.txt','a',encoding='utf-8',errors='ignore') as f:
    for row in data:
        f.writelines(f'{row[0]} | {row[1]} | {row[2]}\n')

        
try:
    with open("C:/Users/USER/OneDrive/Desktop/GSAT.txt","r",encoding='utf-8',errors='ignore') as f:
        for row in f:
            if not row.strip():
                continue
            if len(row) < 3:
                continue
            if 'ERROR' in row:
                print(f'Tên file: {f.name}')
                date, status, amount = row.strip().split('|')
                print(row)
except FileNotFoundError as e:
    print(f'Lỗi: {e}')