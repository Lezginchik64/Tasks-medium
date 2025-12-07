import requests


def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    return requests.get(url).json()['current_weather']


saratov_coords = (51.53, 46)
coords = (51.60, 46.02)
weather = get_weather(*saratov_coords)
weather2 = get_weather(*coords)
print(f"Температура в Саратове: {weather['temperature']}°C, Ветер: {weather['windspeed']} км/ч")
print(f"Температура: {weather2['temperature']}°C, Ветер: {weather2['windspeed']} км/ч")
