import pandas

def drop_duplicate (df):
    df = df.drop_duplicates(subset=['email'], keep='first',inplace=True)
    
if __name__ == '__main__':
    df = pandas.read_csv('data.csv',encoding='utf-8',header=0)
    print(f'Dataframe gốc ban đầu có {df.shape[0]} dòng')
    print(df)
    drop_duplicate(df)
    print(f'Dataframe sau khi xóa duplicate còn {df.shape[0]} dòng')
    print(df)