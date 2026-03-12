import csv
from datetime import * 
# Ghi file .txt
try:
    lines = ['Đây là dòng 1\n','Đây là dòng 2\n']
    name  = 'Hiếu'
    age = 25
    with open("C:/Users/USER/OneDrive/Desktop/note/note_py/log.txt",mode='w',encoding='utf-8') as f:
        f.writelines(lines)
        f.write(f'{name}\n')
        f.write(f'{age}\n')
except FileNotFoundError as e:
    print(f'Lỗi: {e}')
# Đọc file .txt
try:
    with open("C:/Users/USER/OneDrive/Desktop/note/note_py/log.txt",mode='r',encoding='utf-8') as f:
        for row in f:
            row  = row.strip()
            if not row:
                continue
            print(row)   
except FileExistsError as e:
    print(f'Lỗi: {e}')
except FileNotFoundError as e:
    print(f'Lỗi: {e}')
except Exception:
    print('Lỗi khác')

# Đọc file .csv
try:
    with open("C:/Users/USER/OneDrive/Desktop/note/note_py/annual-enterprise-survey-2024-financial-year-provisional.csv",mode='r',encoding='utf-8') as f:
        reader = csv.DictReader(f) # Nếu như các cột ngăn cách nhau bằng dấu ';': csv.DictReader(f,delimiter=';')
        row_count = 0
        for row in reader:
            row_count += 1
            if not row:
                continue
            if len(row) < 10:
                print(f'Dòng thứ {row_count} thiếu cột')
                continue
            print(row) # In ra cột Year có thể dùng cách khác row['Year'] hoặc row.get('Year') => Nếu in cả thì: print(row)
        print(f'Số dòng: {row_count}')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')

# Parse time (strptime) và strftime
try: 
    date_str = '2026-03-11'
    dt = datetime.strptime(date_str,"%Y-%m-%d")
    print(dt.strftime("%d/%m/%y")) # => đổi từ định dạng ngày về chuỗi
    print(dt)
except Exception as e:
    print(f'Lỗi: {e}')

# Ghi file .csv
# Ghi không có header (writer)
data = (
    ['001','Hieu',25],
    ['002','Hung',39]
)
with open('data.csv',mode='w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name','age'])
    writer.writerows(data) # Mỗi list con trong tuple tương ứng 
# Ghi có header (DictWriter)
with open('data.csv',mode='a',encoding='utf-8',newline='') as f:
    header = ['id','name','age']
    writer = csv.DictWriter(f,fieldnames=header)
    writer.writeheader() # Ghi header nếu chưa có, nếu đã có header rồi thì không cần
    writer.writerow({'id': '003', 'name': 'Hoang', 'age': 29})

with open('data.csv',mode='r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)