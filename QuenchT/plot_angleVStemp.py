import matplotlib.pyplot as plt

# Definisci i valori fissi
temp1 = 800
temp2 = 100
total_steps = 20000000

# Inizializza le liste per i dati
T_values = []
Phi_values = []
Ep_values = []
V_values = []

# Apre il file e legge i dati
with open("thermo.txt", "r") as file:
    # Ignora la prima riga di commento
    next(file)
    
    for line in file:
        # Divide la riga in colonne
        columns = line.strip().split()
        
        # Estrai il valore della temperatura dalla prima colonna
        step = float(columns[0])
        temperature = temp1 + (temp2 - temp1) * step / total_steps
        
        # Estrai l'angolo dalla quarta colonna
        angle = float(columns[3])

        #Estrai il Volume dalla seconda colonna
        volume = float(columns[1])

         #Estrai il potential energy dalla terza colonna
        pe = float(columns[2])
        
        # Aggiungi i valori alle liste
        T_values.append(temperature)
        Phi_values.append(angle)
        Ep_values.append(pe)
        V_values.append(volume)


plt.figure(figsize=(10, 6))
plt.plot(T_values, Phi_values, marker='+', linestyle='')
plt.xlabel('Temperature (K)')
plt.ylabel('$\phi$ (${}^\circ$$)')
plt.title('Pressure = 500 atm')
plt.grid(True)


plt.figure(figsize=(10, 6))
plt.plot(T_values, Ep_values, marker='+', linestyle='')
plt.xlabel('Temperature (K)')
plt.ylabel('Potential Energy (kcal/mol)')
plt.title('Pressure = 500 atm')
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.plot(T_values, V_values, marker='+', linestyle='')
plt.xlabel('Temperature (K)')
plt.ylabel('Volume ($\AA^3$)')
plt.title('Pressure = 500 atm')
plt.grid(True)



# Mostra il grafico
plt.show()

