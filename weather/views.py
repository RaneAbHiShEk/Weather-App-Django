import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=e17611d3d65811e704549cb6ee954f99'
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm()
    cities=City.objects.all()
    weather_data=[]
    for city in cities:

        r=requests.get(url.format(city)).json()
    
        city_weather = {
        'city': city.name,
        'temperature': r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context={'weather_data':weather_data,'form':form}
    print(weather_data)
    return render(request,'weather/weather.html',context)