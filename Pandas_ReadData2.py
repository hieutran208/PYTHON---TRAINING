import pandas

def max_to_min(x):
    return x.max() - x.min()

def max_divide_min (x):
    try:
        if x.min() == 0:
            raise ZeroDivisionError
        else:
            return x.max() / x.min()
    except ZeroDivisionError as e:
        print(f"Lỗi: {e}")
        return 0
    
if __name__ == "__main__":
    df = pandas.read_parquet('demo.parquet',engine='pyarrow')
    df_short = pandas.read_parquet('short_data.parquet',engine='pyarrow')

    # group by theo một hoặc nhiều cột 
    # => tính tổng, đếm số dòng, tính TB, tìm min/max cho cột salary
    print(df.groupby('country')['salary'].sum())
    print(df.groupby(['country','gender'])['salary'].count())
    print(df.groupby(['country','gender'])['salary'].mean())
    print(df.groupby('country')['salary'].min())

    # group by theo một hoặc nhiều cột => Kết hợp nhiều hàm khác nhau
    # Nhiều cột, nhiều hàm cho nhiều cột
    print(df.groupby(['country','gender']).agg({'first_name': 'count', 'salary': 'mean'}))
    # Nhiều cột, nhiều hàm cho một cột
    print(df.groupby(['country','gender']).agg({'salary':['count','sum']}))

    # Sử dụng hàm tự thiết kế
    # Lưu ý: hàm này không truyền tham số, khi đưa vào lệnh nó tự hiểu 
    # dữ liệu truyền vào là mảng gồm dữ liệu salary nhóm theo country
    print(df.groupby('country').agg({'salary': max_to_min}))
    print(df.groupby('country')['salary'].agg(max_divide_min))

    # Tạo cột total chứa tổng salary nhóm theo country
    df['total'] = df.groupby('country')['salary'].transform('sum')
    # Tạo cột mới với hàm tự định nghĩa
    df['max-min'] = df.groupby('country')['salary'].transform(max_to_min)