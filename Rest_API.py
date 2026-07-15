import requests
import pandas

url = "https://www.alphavantage.co/query"

params = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":"IBM",
    "interval":"5min",
    "outputsize":"full",
    "apikey":"demo"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    data = pandas.DataFrame.from_dict(data["Time Series (5min)"], orient="index").reset_index().rename(columns={"index":"Timestamp"})
    print(data)
else:
    print(f"Lỗi trong quá trình kết nối, mã lỗi: {response.status_code}")