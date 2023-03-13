import requests
from django.shortcuts import render
from .models import City


def index(request):
    appid = '72b9615007389dcb29cff9e568aea91a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': city_info }

    return render(request, 'weather/index.html', context)
