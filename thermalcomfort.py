import pyowm
import math
import fangers

def getThermalComfort(indoor_temp, indoor_humidity, coordinateX, coordinateY):

    #Personal OpenWeatherMap API Key
    owm = pyowm.OWM('7c759896dc1e8fdb39b532eeaa14641e')

    # Get weather at coordinates- temp, humidity, windspeed
    observation = owm.weather_at_coords(coordinateX, coordinateY)
    w = observation.get_weather()
    outdoorTemp=w.get_temperature()['temp']-273.15
    outdoorHumidity=w.get_humidity()
    outdoorWindSpeed=w.get_wind()['speed']

    #Calculate the felt temperature
    real_temp=calculate_realfeel(outdoorTemp,outdoorHumidity, outdoorWindSpeed)

    #Get clothing index
    clothing_index= calculate_clothindex(real_temp) 

    #Estimate metobolic rate
    #Seated: 1.1
    #Cooking: 1.8
    metobolic_rate=1.1

    #Calculate thermal comfort using Fanger's method
    return fangers.calculate(indoor_temp, indoor_humidity, metobolic_rate,clothing_index)


def calculate_realfeel(temp,humidity,wind):
    #tested against Australian Bureau of Meteorology formula
    e= humidity/100 * 6.105 * math.exp((17.27*temp)/(237.7+temp))
    real_temp= temp + 0.348 * e - 0.7 * wind + .7/(wind+10) - 4.25
    return real_temp




def calculate_clothindex(temp):
    #Standard indoor clothing for hot weather is .5
    #Standard indoor clothing for cold weather is 1.0
    #There is a linear relationship (refer to ASHRAE standards)

    #Lets say clothing index is 1 at 10C and .5 at 26C. Then...
    index= (temp*-.03125) + 1.3125
    if index > 1:
        return 1
    elif index < .5:
        return .5
    else:
        return index
