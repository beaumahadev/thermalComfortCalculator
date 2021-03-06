import thermalcomfort
import fangers

option=input("lon/lat or enter temp? ")

if(option=="lon/lat"):
    coordinatex=float(input("Latitude? "))
    coordinatey=float(input("Longitude? "))
    weather=thermalcomfort.get_temperature(coordinatex,coordinatey)
    outdoorTemp= weather[0]
    outdoorHumidity= weather[1]
    outdoorWindSpeed= weather[2]
else:
    outdoorTemp= float(input("Out door temperature? "))
    outdoorHumidity= float(input("Out door humidity? "))
    outdoorWindSpeed= float(input("Wind speed? "))

real_feel=thermalcomfort.calculate_realfeel(outdoorTemp,outdoorHumidity,outdoorWindSpeed)
clothing_index=thermalcomfort.calculate_clothindex(real_feel)

print("The real feel temperature is: " + str(real_feel))
print("Your estimated clothing index is: "+ str(clothing_index))

indoorTemp=float(input("Indoor temp? "))
indoorHumidity=float(input("Indoor humidity? "))
metabolic_rate=float(input("Metabolic rate? "))

answer= fangers.calculate(indoorTemp,indoorHumidity,metabolic_rate,clothing_index)

print("Thermal comfort score is: "+ str(round(answer['pmv'],2)) + ", the percent of people dissatisfied is "+ str(round(answer['ppd'])) + ", people are " + answer['comfort'])