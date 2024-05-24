#pip install scikit-fuzzy
#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedents
tempIn = ctrl.Antecedent(np.arange(0, 50), 'Temperature indoor')
tempOut =  ctrl.Antecedent(np.arange(0, 50), 'Temperature outdoor')

# Consequents
fanSpeed = ctrl.Consequent(np.arange(0, 600), 'Fan speed')

# Temperature indoor memberships
tempIn['cold'] = np.where(tempIn.universe < 20, 1 ,fuzz.trimf(tempIn.universe, [15, 20, 25]))
tempIn['medium'] = fuzz.trimf(tempIn.universe, [20, 25, 30])
tempIn['hot'] = np.where(tempIn.universe > 30, 1 ,fuzz.trimf(tempIn.universe, [25, 30, 35]))

# Temperature outdoor memberships
tempOut['cold'] = np.where(tempOut.universe < 20, 1 ,fuzz.trimf(tempOut.universe, [15, 20, 25]))
tempOut['medium'] = fuzz.trimf(tempOut.universe, [20, 25, 30])
tempOut['hot'] = np.where(tempOut.universe > 30, 1 ,fuzz.trimf(tempOut.universe, [25, 30, 35]))

# Fan speed memberships
fanSpeed['zero'] = fuzz.trimf(fanSpeed.universe, [-150, 0, 150])
fanSpeed['slow'] = fuzz.trimf(fanSpeed.universe, [0, 150, 300])
fanSpeed['medium'] = fuzz.trimf(fanSpeed.universe, [150, 300, 450])
fanSpeed['fast'] = fuzz.trimf(fanSpeed.universe, [300, 450, 600])
fanSpeed['max'] = fuzz.trimf(fanSpeed.universe, [450, 600, 750])

# Rule system
# Rules for fan speed
rule1 = ctrl.Rule(tempIn['cold'] & tempOut['cold'], fanSpeed['zero'])
rule2 = ctrl.Rule(tempIn['medium'] & tempOut['cold'], fanSpeed['slow'])
rule3 = ctrl.Rule(tempIn['hot'] & tempOut['cold'], fanSpeed['medium'])
rule4 = ctrl.Rule(tempIn['cold'] & tempOut['medium'], fanSpeed['slow'])
rule5 = ctrl.Rule(tempIn['medium'] & tempOut['medium'], fanSpeed['medium'])
rule6 = ctrl.Rule(tempIn['hot'] & tempOut['medium'], fanSpeed['fast'])
rule7 = ctrl.Rule(tempIn['cold'] & tempOut['hot'], fanSpeed['medium'])
rule8 = ctrl.Rule(tempIn['medium'] & tempOut['hot'], fanSpeed['fast'])
rule9 = ctrl.Rule(tempIn['hot'] & tempOut['hot'], fanSpeed['max'])

# Control System Creation and Simulation
fanSpeed_output = ctrl.ControlSystemSimulation(ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]))

# Enter values to test
indoorTemperature = float(input("Input Ti (Temperature indoor [0, 50°C]): "))
while indoorTemperature < 0 or indoorTemperature > 50:
    try:
      indoorTemperature = float(input("Please input Ti between 0 and 50: "))
    except ValueError:
      print("We expect you to enter a valid integer!")

outdoorTemperature = float(input("Input To (Temperature outdoor [0, 50°C]): "))
while outdoorTemperature < 0 or outdoorTemperature > 50:
    try:
      outdoorTemperature = float(input("Please input To between 0 and 50: "))
    except ValueError:
      print("We expect you to enter a valid integer!")

# Defuzzification
fanSpeed_output.input['Temperature indoor'] = indoorTemperature
fanSpeed_output.input['Temperature outdoor'] = outdoorTemperature

fanSpeed_output.compute()

# View
print(f"\nFan Speed after defuzzyfication (using centroid gravity method): {fanSpeed_output.output['Fan speed']} (RPM)\n")
tempIn.view()
tempOut.view()
fanSpeed.view(sim=fanSpeed_output)
plt.show()