import thermalcomfort
import fangers

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