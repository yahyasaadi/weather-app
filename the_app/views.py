import os
import requests
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import City

# Create your views here.

api_key = os.environ.get('OPEN_WEATHER_API')
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def home(request):

    # # ALL
    # cities = City.objects.all()

    # all_cities = []
    # for city in cities:
    #     results = requests.get(url.format(city, api_key)).json()

    #     # Dict to hold info
    #     temp_in_f = results['main']['temp'] - 273.15
    #     # print(city.continent)
    #     weather_info = {
    #         'city': city,
    #         'description': results['weather'][0]['description'],
    #         'temprature': format(temp_in_f, '.2f'),
    #         'icon': results['weather'][0]['icon']
    #     }
    #     all_cities.append(weather_info)
    
    # AFRICA
    afircan_cities = City.objects.filter(continent='Africa')

    cities_Africa = []
    for city in afircan_cities:
        results = requests.get(url.format(city, api_key)).json()

        # Dict to hold info
        temp_in_f = results['main']['temp'] - 273.15
        weather_info = {
            'city': city,
            'description': results['weather'][0]['description'],
            'temprature': format(temp_in_f, '.2f'),
            'icon': results['weather'][0]['icon']
        }
        cities_Africa.append(weather_info)

    # NORTH AMERICA
    north_american_cities = City.objects.filter(continent='North America')

    cities_N_America = []
    for city in north_american_cities:
        results = requests.get(url.format(city, api_key)).json()

        # Dict to hold info
        temp_in_f = results['main']['temp'] - 273.15
        weather_info = {
            'city': city,
            'description': results['weather'][0]['description'],
            'temprature': format(temp_in_f, '.2f'),
            'icon': results['weather'][0]['icon']
        }
        cities_N_America.append(weather_info)

    # SOUTH AMERICA
    south_american_cities = City.objects.filter(continent='South America')
    cities_S_America = []
    for city in south_american_cities:
        results = requests.get(url.format(city, api_key)).json()

        # Dict to hold info
        temp_in_f = results['main']['temp'] - 273.15
        weather_info = {
            'city': city,
            'description': results['weather'][0]['description'],
            'temprature': format(temp_in_f, '.2f'),
            'icon': results['weather'][0]['icon']
        }
        cities_S_America.append(weather_info)


    # MIDDLE EAST
    middle_eastern_cities = City.objects.filter(continent='Middle East')
    middle_East = []
    for city in middle_eastern_cities:
        results = requests.get(url.format(city, api_key)).json()

        # Dict to hold info
        temp_in_f = results['main']['temp'] - 273.15
        weather_info = {
            'city': city,
            'description': results['weather'][0]['description'],
            'temprature': format(temp_in_f, '.2f'),
            'icon': results['weather'][0]['icon']
        }
        middle_East.append(weather_info)

    
    # EUROPE
    european_cities = City.objects.filter(continent='Europe')
    europe = []
    for city in european_cities:
        results = requests.get(url.format(city, api_key)).json()

        # Dict to hold info
        temp_in_f = results['main']['temp'] - 273.15
        weather_info = {
            'city': city,
            'description': results['weather'][0]['description'],
            'temprature': format(temp_in_f, '.2f'),
            'icon': results['weather'][0]['icon']
        }
        europe.append(weather_info)


    # ASIA
    asian_cities = City.objects.filter(continent='Asia')
    asia = []
    for city in asian_cities:
        results = requests.get(url.format(city, api_key)).json()

        # Dict to hold info
        temp_in_f = results['main']['temp'] - 273.15
        weather_info = {
            'city': city,
            'description': results['weather'][0]['description'],
            'temprature': format(temp_in_f, '.2f'),
            'icon': results['weather'][0]['icon']
        }
        asia.append(weather_info)


    context = {
        'cities_Africa': cities_Africa,
        'cities_N_America': cities_N_America,
        'cities_S_America': cities_S_America,
        'middle_East': middle_East,
        'europe': europe,
        'asia': asia,
        # 'all_cities': all_cities
    }
    return render(request, 'the_app/home.html', context)


def search_city(request):

    weather_info = {}

    if request.method == 'POST':
        city = request.POST['city']
        result = requests.get(url.format(city, api_key)).json()

        if result['cod'] == 200:

            temp_in_f = result['main']['temp'] - 273.15

            weather_info = {
                'city': city,
                'description': result['weather'][0]['description'],
                'temprature': format(temp_in_f, '.2f'),
                'icon': result['weather'][0]['icon']
            }
            return render(request, 'the_app/search.html', context={'weather_info': weather_info})
        else:
            messages.error(request, f'Enter a valid city name!')
            return redirect('home')

            




