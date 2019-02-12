import calculateComfort


#sample values
air_temp=27
humidity=60
met_rate=1.1
clo_index=.5

#Answers taken from CBE Thermal Comfort Calculator: http://comfort.cbe.berkeley.edu/
correct_pmv=.62
correct_ppd=13


calculateComfortAnswer= calculateComfort.calculate(air_temp,humidity,met_rate,clo_index)

if round(calculateComfortAnswer['pmv'],2)==correct_pmv and round(calculateComfortAnswer['ppd'])==correct_ppd:
    print("TEST PASSED")
else:
    print("Got pmv: " + str(round(calculateComfortAnswer['pmv'],2))+ ", was expecting: "+ str(correct_pmv))
    print("Got ppd: " + str(round(calculateComfortAnswer['ppd']))+ ", was expecting: "+ str(correct_ppd))