# thermalComfortCalculator

Calculates thermal comfort using ASHRAE standard PMV/PPD method. Uses GPS coordinates to estimate clothing index. Makes some other assumptions about metabolic rate. 

function calculateComfort uses Fanger's Predicted Mean Vote model for thermal comfort. 
From wikipedia:
```
Fanger's equations are used to calculate the Predicted Mean Vote (PMV) of a large group of subjects 
for a particular combination of air temperature, mean radiant temperature, relative humidity, air speed, 
metabolic rate, and clothing insulation. Zero is the ideal value, representing thermal neutrality, 
and the comfort zone is defined by the combinations of the six parameters for which the PMV is 
within the recommended limits (-0.5<PMV<+0.5). Although predicting the thermal sensation of a 
population is an important step in determining what conditions are comfortable, 
it is more useful to consider whether or not people will be satisfied. 
Fanger developed another equation to relate the PMV to the Predicted Percentage of Dissatisfied (PPD).
```

Results tested against UC Berkely's CBE Thermal Comfort Calculator: http://comfort.cbe.berkeley.edu/


to run: 
`
python test_thermalcomfort.py
`
dependencies: pyowm 
`
pip install pyowm
`
