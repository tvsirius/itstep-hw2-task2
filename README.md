# itstep-hw2-task2
itstep-homeworks2-task2

 Получить данные о погоде по апи.

Сайт и документация: https://www.metaweather.com/api/

 - Сделать запрос по адресу https://www.metaweather.com/api/location/search/?query=kiev
 - Из ответа достать id погодной зоны, по ключу woeid
 - Сделать запрос по адресу https://www.metaweather.com/api/location/{woeid}/
 - Из ответа получить следующие данные: температура, влажность, скорость ветра.


Поскольку сайт  https://www.metaweather.com/api/ не работает то буду разбираться где взять данные о погоде по ссылке:
https://syncwith.com/api/metaweather-api

и буду рабоать с 
https://openweathermap.org/api/one-call-3#multi

используя  Weather API и Geocoding API

ключ в конфиг файле
