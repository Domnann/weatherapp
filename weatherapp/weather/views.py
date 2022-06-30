from django.shortcuts import render
import urllib.request
import json

from numpy import source

def index (request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=ac555068d369bcdef6ee62b69bba9902')
        list_of_data = json.loads(source)
        data= {
            "country_code": str(list_of_data['sys']['country']),
            "coordinates": str(list_of_data['coord']['lon'])+  str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp'])+ "C",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "temp_min": str(list_of_data['main']['temp_min']),
            "temp_max": str(list_of_data['main']['temp_max']),
        }

        print(data)

    else:
        data={}

    return render(request, "main/index.html", data )


