import pandas as pd
import json

def rename_column(df,col1,col2):
    df = df.rename(columns={col1:col2})
    return df

if __name__ == '__main__':
    with open ('exp.json','r',encoding='utf-8-sig') as f:
        data = json.load(f)
    df1 = pd.json_normalize(data,record_path='items',meta=['order_id','customer'])
    df2 = pd.read_csv('data.csv',header=0,encoding='utf-8')
    df3 = pd.read_json('sample_stream.ndjson',lines=True).explode('level','message')
    df3 = df3.rename(columns={'timestamp': 'Timestamp'})
    print(df3)