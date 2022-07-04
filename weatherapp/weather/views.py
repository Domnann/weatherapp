from django.shortcuts import render
import urllib.request
import json
import requests

from numpy import source

def index(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=1931ac61ca79965a84c67a13f81050ac').read()
        
            list_of_data = json.loads(source)

            data = {
                "city_name": str(list_of_data['name']),
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon'])+  ',' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp'])+ "C",
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": str(list_of_data['weather'][0]['icon']),
                "temp_min": str(list_of_data['main']['temp_min']),
                "temp_max": str(list_of_data['main']['temp_max']),
            }

            # print(data)

        else:
            data={}

        return render(request, "weather/index.html", data)

    except:
        _error = {"error" : ("Your Input Is Not Correct!"),}
        return render(request, "weather/index.html", _error)


