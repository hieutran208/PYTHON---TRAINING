import pandas as pd
from modify_col import *

if __name__ == '__main__':
    df = pd.read_json('sample_stream.ndjson',lines=True)
    print(df)
    df = title_col(df,'message')
    print(df)