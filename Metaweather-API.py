import requests

url = "https://www.metaweather.com/api/location/search/?lattlong=20.59,78.96"

#url = "https://www.metaweather.com/api/location/search/?query=chennai"

r = requests.get(url).json()

print(r)

print(r[5]['title'])

