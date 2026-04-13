import pandas as pd

def fill_na (df,col):
    df[col] = df[col].fillna(0)
    
if __name__ == '__main__':
    df = pd.read_csv('data.csv',header=0,encoding='utf-8')
    fill_na(df,'email')
    print(df)