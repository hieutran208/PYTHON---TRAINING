import pandas
def create_bonus_col (lst):
    df = pandas.DataFrame(lst,columns=['student_id','name','age'])
    df['rank_age'] = df['age'].apply(lambda x: 'old' if x > 10 else 'young')
    """
    - df["age"].apply(...) 
    => apply áp dụng hàm đưa vào cho tất cả các giá trị trong cột age
    - lambda x: 'old' if x > 10 else 'young'
    => lambda x: x chính là từng giá trị trong cột age 
    """
    return df
if __name__ == "__main__":
    students = [
        [101,"Ulysses",13],
        [53,"William",10],
        [128,"Henry",6],
        [3,"Henry",11]
    ]
    print(create_bonus_col(students))