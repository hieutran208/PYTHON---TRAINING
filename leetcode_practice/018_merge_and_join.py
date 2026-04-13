"""
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""
import pandas as pd
def left_join (df1,df2,left_key,right_key):
    merge = df1.merge(df2,left_on=left_key,right_on=right_key,how='left')
    return merge
if __name__ == '__main__':
    customers = [
        [1,'Joe'],
        [2,'Henry'],
        [3,'Sam'],
        [4,'Max']
    ]
    
    orders = [
        [1,3],
        [2,1]
    ]
    df1 = pd.DataFrame(customers,columns=['id','name'])
    df2 = pd.DataFrame(orders,columns=['id','customerId'])

    merge = left_join(df1,df2,'id','id')
    print(merge.loc[merge['customerId'].isna(),['id','name']])