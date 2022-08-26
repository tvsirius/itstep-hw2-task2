import requests
from openweather_api import openweather_api
import pprint

lat=30.489772
lon=-99.771335

exclude='minutely,hourly,daily,alerts'

units='metric'

weather_get=requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={openweather_api}&lang=ru&units={units}')



pprint.pprint(weather_get.json())


