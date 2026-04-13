"""
Input:
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+

Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
"""
import pandas

def create_DataFrame (lst):
    df = pandas.DataFrame(lst,columns=['id','age'])
    return(df)

if __name__ == '__main__':
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]
    df = create_DataFrame(student_data)
    print(df)