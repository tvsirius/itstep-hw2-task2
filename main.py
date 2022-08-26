import requests
from openweather_api import openweather_api
import pprint

# lat=30.489772
# lon=-99.771335

city_name,country_code = 'Kiev', 'UA'

location_get=requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={openweather_api}')

pprint.pprint(location_get.json())

lat,lon = location_get.json()[0]['lat'],location_get.json()[0]['lon']

exclude='minutely,hourly,daily,alerts'

units='metric'

weather_get=requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={openweather_api}&lang=ru&units={units}')



pprint.pprint(weather_get.json())


