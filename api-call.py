import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=compact&apikey=CTXZESHGPF6ONDJR'
r = requests.get(url)
data = r.json()

print(data)