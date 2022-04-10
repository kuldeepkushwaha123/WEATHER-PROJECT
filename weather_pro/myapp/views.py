from django.shortcuts import render
from django.contrib import messages
import urllib
import json
# Create your views here.

def Home(request):
    if request.method == "POST":
        city = request.POST.get('city')
        api_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=41a8b82e3e0dbbc247074e5b567007c2').read()
        api_url2 = json.loads(api_url)
        print(api_url2)

        data = {
            'city': city,
            'weather_description': api_url2['weather'][0]['description'],
            'weather_temperature': api_url2['main']['temp'],
            'weather_pressure': api_url2['main']['pressure'],
            'weather_humidity': api_url2['main']['humidity'],
            'weather_icon': api_url2['weather'][0]['icon']

        }
    else:
        data = {
            'city': None,
            'weather_description': None,
            'weather_temperature': None,
            'weather_pressure': None,
            'weather_humidity': None,
            'weather_icon': None,
        }



    return render(request,'index.html',{'data':data})
