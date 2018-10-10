import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&APPID=10552696e7ed12d8b44cf86c7aa9e9e0'
    city = 'Las Vegas'
    r = requests.get(url.format(city))
    print(r.text[:500])
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {

            'city': city.name,
            'temp': r['list'][1]['main']['temp'],
            'temp_min': r['list'][1]['main']['temp_min'],
            'description': r['list'][8]['weather'][0]['description'],
            'icon': r['list'][8]['weather'][0]['icon']


        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)



