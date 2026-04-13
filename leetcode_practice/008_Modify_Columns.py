import pandas as pd

def title_col(df, col):
    # str.title(): viết hoa chữ cái đầu của mỗi từ, các chữ còn lại viết thường
    df[col] = df[col].str.title()
    return df

if __name__ == '__main__':
    df = pd.read_json('sample_stream.ndjson',lines=True).explode('message','level')
    df = title_col(df,'message')
    print(df)