from colorama import Fore, Back, Style
print(Fore.RED+"\n______________________BlueWeather______________________\n\n"+Fore.MAGENTA+"Python Version | https://github.com/akshayitzme\n")
conf=open(".conf","w+")
key=input(Fore.GREEN+">>Enter WeatherBit API Key:")
if key!="":
	conf.write(key)
	conf.close()
	print('\n 	Config Created!\n')
else:
	print(Fore.RED+'Setup Failed \nEnter Valid Key')