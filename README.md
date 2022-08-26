# itstep-hw2-task2
itstep-homeworks2-task2

 Получить данные о погоде по апи.

Сайт и документация: https://www.metaweather.com/api/

 - Сделать запрос по адресу https://www.metaweather.com/api/location/search/?query=kiev
 - Из ответа достать id погодной зоны, по ключу woeid
 - Сделать запрос по адресу https://www.metaweather.com/api/location/{woeid}/
 - Из ответа получить следующие данные: температура, влажность, скорость ветра.

Сайт https://www.metaweather.com/api/ не работал

Код работает с 
https://openweathermap.org/api/one-call-3#multi

использует Weather API и Geocoding API

Необходим API ключ в openweather_api.py
