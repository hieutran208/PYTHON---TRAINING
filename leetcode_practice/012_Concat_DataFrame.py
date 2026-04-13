import pandas as pd

def concat_dataframe (df1,df2):
    df = pd.concat([df1,df2],axis=0)
    return df

if __name__ == '__main__':
    
    df1 = [[1,"Mason",8],
        [2,"Ava",6],
        [3,"Taylor",15],
        [4,"Georgia",17]]

    df2 = [[5,"Leo",7],
        [6,"Alex",7]]
     
    df1 = pd.DataFrame(df1, columns=['student_id',"name","age"])
    df2 = pd.DataFrame(df2, columns=['student_id',"name","age"])
    print(concat_dataframe(df1,df2))