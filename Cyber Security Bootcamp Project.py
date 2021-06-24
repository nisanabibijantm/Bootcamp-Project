import requests

from datetime import datetime

api_key = '87d845b0b6cf29baala73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weatther'][0]['description']
hmdt = api_data['main']['himidity']
wind_spd = api_data['wind']['speed']
Date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("...............................................................")
print("Weather starts for - {} || {}".format(location.upper(), Date_time))
print("...............................................................")

print("Current temperature:{:.2f} deg C".format(temp_city))
print("Current weather desc :", weather_desc)
print("Current Humidity     :", '%')
print("Current wind speed   :", wind_spd, 'knph')
