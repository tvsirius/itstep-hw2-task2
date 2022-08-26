import requests
from openweather_api import openweather_api


lat=lon=0
exclude=0

weather=requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={openweather_api}')