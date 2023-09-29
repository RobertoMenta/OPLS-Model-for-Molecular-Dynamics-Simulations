import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Load data from 'averages.txt' file and skip the first row
data = np.genfromtxt('averages.txt', delimiter='\t', dtype=None, names=True)
linephase = np.genfromtxt('line_phase_Gas-Liquid.txt', dtype=None, names=True)
linephaseVL = np.genfromtxt('line_phase_Glass-Liquid.txt', dtype=None, names=True)


x = [i for i in range(0, 1550)]  
y = [0] * len(x)

        

# Extract columns from the data
temperature = data['Temperature_K']
pressure = data['Pressure_atm']
avg_volume = data['Average_Volume']
avg_pe = data['Average_Potential_Energy']
avg_dihedral = data['Average_Dihedral_Column']

#print(linephase)
temp_phase = linephase['temp']
press_phase = linephase['press']

temp_phaseVL = linephaseVL['temp']
press_phaseVL = linephaseVL['press']


# Plot Temperature vs. Potential Energy with Pressure as color
plt.figure(figsize=(10, 6))
scatter = plt.scatter(temperature, avg_pe, c=np.log(pressure), cmap='viridis', marker='.')
plt.xlabel('Temperature (K)')
plt.ylabel('Average Potential Energy (kcal/mol)')
plt.colorbar(scatter, label='$log$[Pressure (atm)]')

# Plot Temperature vs. Dihedral Column with Pressure as color
plt.figure(figsize=(10, 6))
scatter = plt.scatter(temperature, avg_dihedral, c=np.log(pressure), cmap='viridis', marker='.')
plt.xlabel('Temperature (K)')
plt.ylabel('|$\overline{\phi}$| (${}^\circ$)')
plt.colorbar(scatter, label='$log$[Pressure (atm)]')
plt.plot(x, y, linestyle='dashed', linewidth=0.5)
plt.xlim([80,1520])
plt.ylim([-15,25])


plt.figure(figsize=(10, 6))
scatter = plt.scatter(temperature, pressure, c=np.log(avg_volume), cmap='viridis', marker='.')
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (atm)')
plt.colorbar(scatter, label="$log$[Average Volume ($\AA^3$)]")
plt.plot(temp_phase,press_phase, marker='P', color='red')
plt.plot(temp_phaseVL,press_phaseVL, marker='D', color='blue')
plt.text(300,3300,'Glass',fontsize=14, fontweight='bold')
plt.text(1100,4300,'Liquid',fontsize=14, fontweight='bold')
plt.text(1200,300,'Gas',fontsize=14, fontweight='bold')
plt.xlim([50,1550])
plt.ylim([50,10200])

plt.figure(figsize=(10, 6))
scatter = plt.scatter(temperature, pressure, c=np.abs(avg_dihedral), cmap='viridis', marker='.')
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (atm)')
plt.colorbar(scatter, label="|$\overline{\phi}$| (${}^\circ$)")
plt.xlim([50,1550])
plt.ylim([50,10200])
plt.plot(temp_phase,press_phase, marker='P', color='red')
plt.plot(temp_phaseVL,press_phaseVL, marker='D', color='blue')
plt.text(300,3300,'Glass',fontsize=14, fontweight='bold')
plt.text(1100,4300,'Liquid',fontsize=14, fontweight='bold')
plt.text(1200,300,'Gas',fontsize=14, fontweight='bold')



# Show all plots
plt.show()

