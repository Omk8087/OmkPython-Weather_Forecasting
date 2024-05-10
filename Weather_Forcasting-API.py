import requests
import datetime
import json

base_url = "http://api.openweathermap.org/data/2.5/weather?"

api_key = "0c155b577a79d5b3b67eff0ee565c1e5" #open('api_key' , 'r').read()
city = input('Enter City Name:')

url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()

########api_data = response.json()
####print(response)


if response ['cod'] == '404':
    print('Invalid city {}, Please check yourcity name'.format(city))
else:
    temp_location = ((response ['main']['temp'])-273.15)
    weather_desc = response['weather'][0]['description']
    hmdt = response['main']['humidity']
    wind_spd = response['wind']['speed']
    date_time = datetime.datetime.now().strftime("%d %b %Y || %I:%M:%S %p")
    

print("---------------------------------------------------------------------------")    
print("weather stats for-{}||{}".format(city.upper(),date_time))

print("---------------------------------------------------------------------------")    
print("Current Temprature is:{:.2f}deg c".format(temp_location))

print("current weather desc:" ,weather_desc)
print("Current Humadity:" ,hmdt , '%')
print("current wind speed:" ,wind_spd , 'kmph')



