import requests
from openweather_api import openweather_api
import pprint

# city_name,country_code = 'Kiev', 'UA'

while True:
    input_field = input('Пожалуйста введите название города, или города и код страны, или города, штата и страны через запятую:')
    try:
        input_decode = input_field.strip().replace(', ', ',').replace(' ,', ',').replace('  ', ' ').split(',')
        if len(input_decode) == 3:
            (city_name, state_code, country_code) = input_decode
            location_get = requests.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={openweather_api}')
        elif len(input_decode) == 2:
            (city_name, country_code) = input_decode
            location_get = requests.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={openweather_api}')
        elif len(input_decode) == 1:
            city_name = input_decode[0]
            location_get = requests.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={openweather_api}')
        else:
            print('Город не найден, или данные введены некорректно, пожалуйста повторите запроос')
            continue
        lat, lon = location_get.json()[0]['lat'], location_get.json()[0]['lon']
        break
    except:
        pass
    print('Город не найден, или данные введены некорректно, пожалуйста повторите запроос')


exclude = 'minutely,hourly,daily,alerts'
units = 'metric'

weather_get = requests.get(
    f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={openweather_api}&lang=ru&units={units}')

# pprint.pprint(location_get.json())
# pprint.pprint(weather_get.json())

try:
    print(f'Данные о погоде в городе {location_get.json()[0]["local_names"]["ru"]}:')
except:
    print(f'Данные о погоде в городе {input_field}:')

print(f'{weather_get.json()["current"]["weather"][0]["description"].capitalize()}, температура: {weather_get.json()["current"]["temp"]} C, влажность: {weather_get.json()["current"]["humidity"]}, скорость ветра: {weather_get.json()["current"]["wind_speed"]}')
