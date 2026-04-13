import pandas

def drop_nan (df):
    df = df.dropna(axis=0,how='any',subset=['email'])
    return df

if __name__ == '__main__':
    df = pandas.read_csv('data.csv',encoding='utf-8',header=0)
    df = drop_nan(df)
    print(df)
