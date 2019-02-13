import thermalcomfort

coordinateX= 22.428005
coordinateY= 114.210902
indoorTemp= 27
indoorHumidity= 60

answer= thermalcomfort.getThermalComfort(indoorTemp,indoorHumidity,coordinateX,coordinateY)


print("For location: (" + str(coordinateX) + "),(" + str(coordinateY) + ")")
print("With indoor temperature: " + str(indoorTemp))
print("With indoor humidity: " + str(indoorHumidity))
print("Thermal comfort score is: "+ str(round(answer['pmv'],2)) + " and the percent of people dissatisfied is "+ str(round(answer['ppd'])))