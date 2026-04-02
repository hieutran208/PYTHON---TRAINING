import pandas as pd

if __name__ == '__main__':
    df = pd.read_parquet('demo.parquet',engine='pyarrow')
    df_short = pd.read_parquet('short_data.parquet',engine='pyarrow')
    keys1 = ['id','salary']
    keys2 = ['id','salary']
    print(pd.merge(df,df_short,how='left',left_on=keys1,right_on=keys2,indicator=True))
    # indicator=True: biết được mỗi dòng đến từ đâu (left_only, right_only, both)
    # Phần kết quả: Các cột cùng tên => nằm trong khóa JOIN thì giữ nguyên tên cột, không trong khóa JOIN thì tự động thêm hậu tố để phân biệt
    df.set_index('id',inplace=True)
    df_short.set_index('id',inplace=True)
    print(df.join(df_short,how='inner'))