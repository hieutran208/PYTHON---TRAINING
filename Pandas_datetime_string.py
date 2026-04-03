import pandas
from datetime import *
if __name__ == "__main__":
    df_raw = pandas.read_parquet('raw_data.parquet',engine='pyarrow')
    df = pandas.read_parquet('bank_data.parquet',engine='pyarrow')
    
    # XỬ LÝ DATETIME
    # errors='coerce': Parse lỗi => Chuyển thành NaT thay vì báo lỗi (giống NaN nhưng cho thời gian)
    df['Date'] = pandas.to_datetime(df['Date'], errors='coerce')
    df_raw['birthdate'] = pandas.to_datetime(df_raw['birthdate'],errors='coerce')
    print(df_raw['birthdate'].dt.year) # Trích xuất năm
    print(df['Date'].dt.month) # Trích xuất tháng
    print(df['Date'].dt.day) # Trích xuất ngày
    print(df['Date'].dt.strftime('%m-%Y')) # Trích xuất theo tháng-năm (nhớ phải khớp định dạng)
    print(df.loc[df['Date'].dt.day == 13]) # Lọc theo ngày

    # XỬ LÝ STRING
    # Tạo cột name bằng cách ghép 2 cột first_name và last_name
    df_raw['name'] = df_raw['first_name'] + ' ' + df_raw['last_name']
    # Trả về độ dài từng dòng trong cột
    print(df_raw['name'].str.len())
    # Chuyển cột name về chữ thường
    print(df_raw['name'].str.lower()) 
    # Chuyển cột name về chữ hoa
    print(df_raw['name'].str.upper()) 
    # Loại bỏ khoảng trắng đầu - cuối
    print(df_raw['name'].str.strip())
    # Tách cột name thành 2 cột first_name_split và last_name_split dựa vào khoảng trắng
    # (vẫn giữ cột name, expand=True để trả về DataFrame)
    df_raw[['first_name_split','last_name_split']] = df_raw['name'].str.split(' ', expand=True)
    # Lấy ra phần khớp với điều kiện (điều kiện phải đặt trong ngoặc đơn)
    print(df['Date'].astype(str).str.extract(r'(\d{4})'))
    print(df_raw.columns)
    # Lọc dữ liệu dựa vào điều kiện trên text (= where Acquired by LIKE '%Sunwest Bank%')
    print(df.loc[df['Acquired by'].str.contains('Sunwest Bank',na=False)])
    # Lọc dữ liệu dựa trên ký tự bắt đầu 
    # (na=False => nếu là na thì coi như ko thỏa mãn điều kiện thay vì trả ra lỗi)
    print(df_raw.loc[df_raw['ip_address'].str.startswith('192',na=False)])
    # Lọc dữ liệu dựa trên ký tự kết thúc
    print(df_raw.loc[df_raw['birthdate'].astype(str).str.endswith('13',na=False)])