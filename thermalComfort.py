import pyowm


#Personal OpenWeatherMap API Key
owm = pyowm.OWM('7c759896dc1e8fdb39b532eeaa14641e')
# Get weather at coordinates- temp, humidity, wind chill
observation = owm.weather_at_coords(22.428005, 114.210902)
w = observation.get_weather()
tempC=w.get_temperature()['temp']-273.15
humidity=w.get_humidity()

#Calculate Real Feel

#Estimate clothing index from Real Feel
#Very hot weather temp is .5, Very cold is 1.0, linear relationship with temp inbetween


#Estimate metobolic rate
#Seated: 1.0
#Cooking: 1.8


#Calculate thermal comfort 




print(tempC)
print(humidity)    