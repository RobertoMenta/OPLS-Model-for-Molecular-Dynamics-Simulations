import os
import numpy as np

# Function to extract data from a file
def extract_data(file_path):
    volume = []
    potential_energy = []
    dihedral_column = []

    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line (comment)
        for line in lines:
            data = line.split()
            # Temperature is not appended to the 'temperature' list
            volume.append(float(data[1]))
            potential_energy.append(float(data[2]))
            dihedral_column.append(float(data[3]))

    return volume, potential_energy, dihedral_column

# Get a list of all folders in the current directory
folders = [folder for folder in os.listdir() if os.path.isdir(folder)]

# Initialize dictionaries to store average data
averages = {}  # Dictionary to store averages for each folder

# Create a text file to store the results
output_file = open('averages.txt', 'w')

# Loop through folders, process data, and calculate averages
for folder in folders:
    folder_parts = folder.split('_')
    if len(folder_parts) != 2:
        continue  # Skip folders that do not have the expected format (e.g., '100K_5000atm')

    temperature_str, pressure_str = folder_parts
    temperature = float(temperature_str[:-1])  # Remove 'K' from temperature string
    pressure = float(pressure_str[:-3])  # Remove 'atm' from pressure string

    # Check if thermo.txt exists in the folder
    file_path = os.path.join(folder, 'thermo.txt')
    if not os.path.exists(file_path):
        continue  # Skip this folder if thermo.txt doesn't exist

    # Load data from the thermo.txt file in the folder
    vol, pe, dihedral = extract_data(file_path)

    # Calculate the averages
    avg_vol = np.mean(vol)
    avg_pe = np.mean(pe)
    avg_dihedral = np.mean(dihedral)

    # Store the averages in the dictionary
    averages[folder] = {
        'Temperature (K) from Folder': temperature,
        'Pressure (atm)': pressure,
        'Average Volume': avg_vol,
        'Average Potential Energy': avg_pe,
        'Average Dihedral Column': avg_dihedral
    }

# Write the average data to the text file
output_file.write("Folder\tTemperature (K)\tPressure (atm)\tAverage Volume\tAverage Potential Energy\tAverage Dihedral Column\n")
for folder, data in averages.items():
    output_file.write(f"{folder}\t{data['Temperature (K) from Folder']}\t{data['Pressure (atm)']}\t{data['Average Volume']}\t{data['Average Potential Energy']}\t{data['Average Dihedral Column']}\n")

# Close the output file
output_file.close()

