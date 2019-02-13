import pyowm
import fangers

def getThermalComfort(indoorTemp, indoorHumidity, coordinateX, coordinateY):
    #Personal OpenWeatherMap API Key
    owm = pyowm.OWM('7c759896dc1e8fdb39b532eeaa14641e')
    # Get weather at coordinates- temp, humidity
    observation = owm.weather_at_coords(coordinateX, coordinateY)
    w = observation.get_weather()
    outdoorTemp=w.get_temperature()['temp']-273.15
    outdoorHumidity=w.get_humidity()

    #To Do: Calculate Real Feel
    realTemp=outdoorTemp

    #Standard indoor clothing for hot weather is .5
    #Standard indoor clothing for cold weather is 1.0
    #There is a linear relationship (refer to ASHRAE standards)

    #Lets say clothing index is 1 at 5C and .5 at 26C. Then...

    clothing_index= (realTemp*-.0238) + 1.12
    

    #Estimate metobolic rate
    #Seated: 1.1
    #Cooking: 1.8
    metobolic_rate=1.1

    #Calculate thermal comfort 

    return fangers.calculate(indoorTemp, indoorHumidity, metobolic_rate,clothing_index)


