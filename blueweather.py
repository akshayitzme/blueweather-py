# -*- coding: utf-8 -*-
import requests, sys
from colorama import Fore, Back, Style
conf= open(".conf", "r")
apiKey= conf.read()
def showWeather():
    try:
        city= input(Fore.GREEN+'>> Enter City Name:')
        weather= requests.get(url = 'https://api.weatherbit.io/v2.0/current?', params = {'city':city , 'key': apiKey})
        data= weather.json()
        temp= data['data'][0]['temp']
        cname= data['data'][0]['city_name']
        cCode= data['data'][0]['country_code']
        desc= data['data'][0]['weather']['description']
        appTemp= data['data'][0]['app_temp']
        humid= data['data'][0]['rh']
        ws= int(data['data'][0]['wind_spd'])

        #Print Data 
        print('\n'+cname+','+cCode)
        print(Fore.YELLOW+desc)
        print(Fore.CYAN+"Temperature:",temp,'°C')
        print("Feels Like:",appTemp,'°C')
        print('Humidity:', humid, "%")
        print('Wind Speed:', round(ws*3.6),'km/h')
    except:
        print("Error Program Terminated\n   >>Check Internet Connection\n   >>Enter Valid City Name ")
print(Fore.RED+"\n______________________BlueWeather______________________\n\n"+Fore.MAGENTA+"Python Version | https://github.com/akshayitzme\n")
showWeather()


