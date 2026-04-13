import pandas
def title_col(df, col):
    # str.title(): viết hoa chữ cái đầu của mỗi từ, các chữ còn lại viết thường
    df[col] = df[col].str.title()
    return df
