import pandas
import json
data = {
    "name": ["An", "Bình"],
    "age": [23, 28],
    "salary": [1000, 2000]
}
df = pandas.DataFrame(data)
print(df.shape)
df.to_csv('data.csv',mode='w',encoding='utf-8-sig',columns=["name","age"],index=False,sep='\t') # Ghi dataframe vào file data.csv
df1_csv = pandas.read_csv("C:/Users/USER/OneDrive/Desktop/note/note_py/data.csv",header=0,sep='\t') # header = 0: Lấy dòng 0 
df2_csv = pandas.read_csv("data.csv", header=None, names=["name","age","city"],sep='\t') # Nếu muốn chỉ định tên cột
df3_csv = pandas.read_csv("data.csv", header=0, sep='\t') # sep: File dùng tab (\t) để ngăn các cột thay vì dấu phẩy như mặc định 
df4_csv = pandas.read_csv("data.csv",header=0,encoding="utf-8",sep='\t') # encoding: Chuẩn hóa dữ liệu tiếng Việt
df5_csv = pandas.read_csv("data.csv",header=0,usecols=["name","age"],sep='\t') # usecols: Chỉ đọc 1 số cột
df6_csv = pandas.read_csv("data.csv",header=0,nrows=2,sep='\t') # nrows = n: Chỉ đọc n dòng đầu
print(pandas.read_csv('data.csv',header=0,encoding='utf-8',index_col=0,sep='\t')) 

for chunk in pandas.read_csv("data.csv",chunksize=2,sep='\t'): # chucksize: số dòng trên mỗi lần đọc
    print("Số dòng:", len(chunk))
    print(chunk)

data_json = [
 {"id":1,"name":"An"},
 {"id":2,"name":"Binh"}
]
df_json = pandas.DataFrame(data_json)
df_json.to_json('exp.json', mode='w',orient='records',force_ascii=False,lines=True)
print(pandas.read_json('exp.json',lines=True))

nested_data = [
 {
   "order_id":1,
   "customer":"An",
   "items":[
      {"product":"A","price":100},
      {"product":"B","price":200}
   ]
 }
]
#df_nested_json = pandas.DataFrame(nested_data)
#df_nested_json.to_json('exp.json',orient='records',force_ascii=False,indent=4)
with open('exp.json',mode='w',encoding='utf-8-sig') as f:
    json.dump(nested_data,f,ensure_ascii=False,indent=4)
with open('exp.json',mode='r',encoding='utf-8-sig') as f:
    data = json.load(f)
df = pandas.json_normalize(data,
                           record_path="items", # Chỉ định: lấy list items làm bảng chính
                           meta=['order_id', 'customer']) # Lấy thêm các cột thông tin từ level cha
print(df)

df_parquet = pandas.read_parquet('userdata.parquet',engine="pyarrow")
df_parquet[3:5].to_parquet('demo.parquet',index=False) # [3:5] => Lấy dòng từ 3-4
print(pandas.read_parquet('demo.parquet')["first_name"]) # Lấy cột "first_name"
print(df_parquet["first_name"].value_counts(normalize=True)) # value_counts: Đếm số lần xuất hiện của từng giá trị
# nunique: Đưa ra tổng số các giá trị khác nhau => Output: 120
print(df_parquet['country'].nunique()) 
# unique: Đưa ra danh sách các giá trị khác nhau => Output: danh sách các giá trị khác nhau
print(df_parquet['country'].unique()) 

