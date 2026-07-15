import pandas
import json
import openpyxl
import xlrd
import pyarrow

"""
    **Lưu ý khi tạo Dataframe từ dữ liệu đầu vào:**
    - Nếu dữ liệu chưa có key (dưới dạng list of list): 
        pandas.Dataframe(data, columns=[col1,col2,...])
    - Nếu dữ liệu đã có key: chỉ cần 
        pandas.Dataframe(data):
    VD1: data = [
    {"id":1,"name":"An"},
    {"id":2,"name":"Binh"}
    ]
    VD2: data = {
        "name": ["An", "Bình"],
        "age": [23, 28],
        "salary": [1000, 2000]
    }
    - Khi đã dùng các hàm read_... của Pandas thì không cần tự tạo DataFrame nữa
"""

# ----------File .csv------------
# Dùng r"" trước đường dẫn để Python không hiểu \U, \n, \t là ký tự escape.
# to_csv
#df_to_csv = pandas.read_csv(r"C:\Users\hieutt.portal\Desktop\CODE\PYTHON_TRAINING\sample_data.csv")
#df_to_csv.to_csv(r"C:\Users\hieutt.portal\Desktop\CODE\PYTHON_TRAINING\data.csv", mode='a', index=False, header=False, lineterminator="\n")

# read_csv
df_csv = pandas.read_csv('data.csv', header=0)
df_csv = df_csv.rename(
    columns={
        "id":"ID",
        "name":"NAME",
        "email": "EMAIL"
    }
)
for chunk in pandas.read_csv('demo.csv', header=0, usecols=['product','quarter_1','quarter_2','quarter_3','quarter_4'], chunksize=5):
    print(f"Số dòng 1 chunk đọc được: {len(chunk)}")
    print(chunk)
print(df_csv)

# ----------File .json (xem thêm cả trong phần xử lý dữ liệu json)------------

# json_normalize
with open('exp.json',mode='r',encoding='utf-8-sig') as f:
    data=json.load(f)
data = pandas.json_normalize(data,record_path=["items"],meta=["order_id","customer"])
print(data)
# read_json
print(pandas.read_json('airports.json', encoding='utf-8-sig'))
# Đọc, ghi file ndjson => chỉ loại file này mới cần thêm line=True
print(pandas.read_json('sample_stream.ndjson', lines=True).explode("level"))

# ----------File excel------------
data_excel_1 = pandas.read_excel('file_example_XLSX.xlsx', sheet_name="Sheet1")
data_excel_2 = pandas.read_excel('file_example_XLS.xls', sheet_name="Sheet1")
print(data_excel_1)

# ----------File parquet------------
data_parquet = pandas.read_parquet('raw_data.parquet')
# Ghi vào file parquet: data_parquet.to_parquet("bank_data.parquet", index=False)
print(data_parquet)