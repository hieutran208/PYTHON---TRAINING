import pandas as pd

def loc_bigcountry (df):
    dfc = df.loc[(df['area'] > 300000) | (df['gdp'] > 1000000000000), ['name','area','gdp']]
    # Lưu ý: toán tử | cần dấu ngoặc đơn cho từng điều kiện, loc phải ở dạng .loc[] thay vì .loc()
    return dfc
if __name__ == '__main__':
    world = [
        ["Afghanistan", "Asia",   652230,  25500100,   20343000000],
        ["Albania",     "Europe", 28748,   2831741,    12960000000],
        ["Algeria",     "Africa", 2381741, 37100000,   188681000000],
        ["Andorra",     "Europe", 468,     78115,      3712000000],
        ["Angola",      "Africa", 1246700, 20609294,   100990000000]
    ]
    df = pd.DataFrame(world, columns=['name','continent','area','population','gdp'])
    print(df)
    df = loc_bigcountry(df)
    print(df)