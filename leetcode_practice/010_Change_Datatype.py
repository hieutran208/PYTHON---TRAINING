"""
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
Write a solution to correct the errors:

The grade column is stored as floats, convert it to integers.
"""
import pandas as pd

def change_datatype(df,col):
    df[col] = df[col].astype(int)
    return df

if __name__ == '__main__':
    students = [[1, "Ava", 6, 73.0], [2, "Kate", 15, 87.0]]
    df = pd.DataFrame(students, columns=['student_id','name','age','grade'])
    df = change_datatype(df,'grade')
    print(df['grade'].dtypes)