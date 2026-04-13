"""
Hàm .melt() để chuyển đổi dữ liệu bảng từ dạng wide sang long

CẤU TRÚC:

- df.melt(  id_vars = 'cột giữ nguyên - khóa định danh>', 
            value_vars = ['col_1','col_2',...=> Các cột được 'chảy' thành 1 cột duy nhất ], 
            var_name ='<tên cột mới chứa các tên cột gốc>', 
            value_name ='<tên cột mới chứa giá trị, số liệu tương ứng>'   )

- TH nếu một trong các loại trên không có cột (VD id_vars không có cột) => id_vars=None

- Input:
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+

- Output:
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
"""
import pandas as pd

def meltTable (df):
    df = df.melt(id_vars = 'product',
                 value_vars = ['quarter_1','quarter_2','quarter_3','quarter_4'],
                 var_name = 'quarter',
                 value_name= 'sales')
    return df
if __name__ == '__main__':
    df = pd.read_csv('demo.csv',header=0,encoding='utf-8',index_col=False)
    print(f'INPUT \n {df}')
    df = meltTable(df)
    print(f"OUTPUT\n {df}")
    
