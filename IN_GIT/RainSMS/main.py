import requests
lat = 33.130280
lon = 35.775719
API_key = "69f04e4613056b159c2761a9d9e664d2"

website = "https://api.openweathermap.org/data/3.0/onecall?"

request = requests.get(url= website, params={"lon":lon, "lat":lat, "APPID":API_key})
weather_json = request.json()
print(weather_json)
