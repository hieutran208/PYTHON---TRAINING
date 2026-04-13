import pandas as pd

if __name__ == '__main__':
    data = [
        ["Tatiana",  "Snake",   98, 464],
        ["Khaled",   "Giraffe", 50, 41],
        ["Alex",     "Leopard", 6,  328],
        ["Jonathan", "Monkey",  45, 463],
        ["Stefan",   "Bear",    100, 50],
        ["Tommy",    "Panda",   26, 349]
    ]
    df = pd.DataFrame(data,columns=['name','species','age','weight'])
    # Sắp xếp giá trị theo yêu cầu: df.sort_values(by ='<cột dùng làm điều kiện sắp xếp>',ascending=True/False)
    df = df.sort_values(by=['age','weight'],ascending=False)
    print(df)