import os
try:
  import requests
  import colorama
except ImportError:
  print ("Trying to Install required module: requests\n")
  os.system('pip3 install requests')
  os.system('pip3 install colorama')
import requests
from colorama import Fore, Back, Style
print(Fore.RED+"\n______________________BlueWeather______________________\n\n"+Fore.MAGENTA+"Python Version | https://github.com/akshayitzme\n")
conf=open(".conf","w+")
key=input(Fore.GREEN+">>Enter WeatherBit API Key:")
if key!="":
	conf.write(key)
	conf.close()
	print('\n 	Config Created!\n\n Running BlueWeather')
	os.system('python blueweather.py')
else:
	print(Fore.RED+'Setup Failed \nEnter Valid Key')