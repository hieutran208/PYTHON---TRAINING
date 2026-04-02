import pandas as pd

df = pd.read_parquet('userdata.parquet',engine='pyarrow')
df_demo = pd.read_parquet('demo.parquet',engine='pyarrow')
df_raw = pd.read_parquet('raw_data.parquet',engine="pyarrow")

print(df['country']) # Đưa ra 1 cột

print(df[['first_name','last_name']]) # Đưa ra 2 hoặc nhiều cột

print(df[2:10]) # Chọn dòng từ 2-9

# Lọc theo điều kiện và chọn tên cột: df.loc[<điều kiện lọc>, [cột1, cột2,....]]
print(df.loc[df['country'] == 'Indonesia',['first_name', 'last_name','country']])

df.loc[df['country'] == 'Indonesia','country'] = 'INDONESIA' # Update giá trị bằng loc

print(df.loc[1:3,['first_name','country']]) # Lấy các dòng từ 1 đến 3, 2 cột 'first_name' và 'country'

print(len(df.loc[df['country'] == 'INDONESIA', 'country'])) # Đếm số dòng có 'country' = 'INDONESIA'

# Lọc theo vị trí số: df.iloc[<vị trí dòng>, <vị trí cột>] (iloc chỉ nhận số hàng và số cột)
print(df.iloc[1:3,:5]) 

# Kết hợp nhiều điều kiện (& = AND, | = OR)
# Lưu ý: Mỗi điều kiện phải đặt trong dấu ngoặc đơn
print(df.loc[(df['country'] == 'INDONESIA') & (df['first_name'] == 'Bobby'),['first_name', 'country']])

print(df.loc[(df['country'] == 'Canada') | (len(df['country']) > 8), ['country']].value_counts())

# Lọc theo danh sách
print(df.loc[df['country'].isin(['Canada','Portugal']),['last_name','country']])

# Lọc theo khoảng
print(df.loc[df['id'].between(8,10),['id','first_name']])

# Lọc bằng câu query
print(df[['id','last_name','country']].query("country == 'Canada' and last_name == 'Snyder'"))

# Điều kiện lọc có dùng biến bên ngoài
x = 10
print(df.query("id < @x"))

# Xử lý giá trị NaN (giá trị bị thiếu)

# Kiểm tra giá trị NaN, trả về kết quả True/False
print(df['salary'].isna()) # Các dòng có giá trị bị thiếu sẽ trả về True
print(df[['salary','country']].notna().value_counts()) # notna() ngược lại với isna()

# Đếm số giá trị bị thiếu 
print(df['salary'].isna().sum()) # Kiểm tra một cột => Output: 68
print(df.isna().sum()) # Kiểm tra toàn bảng 

# Tìm ra dòng bị thiếu, lọc dòng không thiếu giá trị
print(df.loc[df['salary'].isna(), ['id','country']])
print(df[df['salary'].notna()]) 

# Xóa dòng, cột bị thiếu giá trị với dropna()
# Xóa tất cả các dòng thiếu giá trị ở cả 2 trường comments và salary
df_demo = df_demo.dropna(axis=0,how='all',subset=['comments','salary'])
# Xóa tất cả các dòng thiếu giá trị ở một trong hai trường comments hoặc salary
df_demo = df_demo.dropna(axis=0,how='any',subset=['comments','salary'])
# Xóa tất cả các cột không có giá trị ở cả 2 dòng 5 và 6
df_demo = df_demo.dropna(axis=1,how='all',subset=[5,6])
# Xóa tất cả các cột không có giá trị ở một trong hai dòng 5 hoặc 6
df_demo = df_demo.dropna(axis=1, how='any',subset=[5,6])

# Thêm giá trị vào nơi bị thiếu với fillna()
# Điền giá trị mặc định 'Unknown' nếu cột country thiếu giá trị
df_raw['country'] = df_raw['country'].fillna('Unknown')
# Điền vào giá trị TB nếu thiếu giá trị
df_raw['salary'] = df_raw['salary'].fillna(df_raw['salary'].mean(skipna=True))
# Điền vào giá trị gần nhất phía trước
df_raw['gender'] = df_raw['gender'].ffill()
# Điền vào giá trị gần nhất phía sau
df_raw['gender'] = df_raw['gender'].bfill()

# Xóa, đổi tên cột
df_demo = df_demo.drop(columns=['cc','comments']) # Mặc định inplace = True (sửa trực tiếp DataFrame gốc)
df_demo = df_demo.rename(columns={'birthdate': 'birth_date','registration_dttm': 'registration_time'})