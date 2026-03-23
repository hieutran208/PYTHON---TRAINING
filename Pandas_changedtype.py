import pandas as pd

df1 = pd.DataFrame({
    "age": ["25", "30", "28"]
})
df1 = df1.astype({"age":int}) # Nhiều cột: df.astype({"age":int, "salary": int})
print(df1.dtypes) # Output: age int64 dtype: object

df2 = pd.DataFrame([
    {"name": "An", "age": 25},
    {"name": "Binh", "age": 30}
])
print(df2.to_dict(orient='records'))