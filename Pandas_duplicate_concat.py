import pandas

if __name__ == '__main__':
    df = pandas.read_parquet('bank_data.parquet',engine='pyarrow')
    # XỬ LÝ DÒNG TRÙNG
    # df.duplicated() => Trả về True/False cho từng dòng
    # df.duplicated().sum() => đếm số dòng trùng
    # subset=['Bank','City'] => Chỉ xét cho 2 cột Bank và City
    # keep => 'first'/'last': giữ dòng đầu/cuối; False: Tất cả dòng trùng đều False
    print(df.duplicated(subset=['Bank','City'], keep='first').sum())
    # Xóa dòng trùng
    df.drop_duplicates(subset=['Bank','City'], keep='last')

    # NỐI 2 DATAFRAME
    """
    Cấu trúc chung: pandas.concat([df1, df2], axis = 0/1)
    - axis = 0: Nối theo dòng (giống UNION ALL trong SQL)
    - axis = 1: Nối các cột theo index => Dùng thêm tham số ignore_index=True để tránh trùng index
    """
    