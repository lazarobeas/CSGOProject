import pandas as pd
import os

# The directory containing all the CSV files
csv_dir = 'C:\\Users\\Lazaro B\\Documents\\GitHub\\CSGOProject\\data\\Espionage'

# List to store the player data
kscerato_data = []

# Loop through each CSV file in the directory
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        # Read the CSV file into a DataFrame
        filepath = os.path.join(csv_dir, filename)
        df = pd.read_csv(filepath)

        # Filter out rows related to KSCERATO
        kscerato_rows = df[df['Nickname'] == 'Cabbi']

        # If there are such rows, append them to the list
        if not kscerato_rows.empty:
            kscerato_data.append(kscerato_rows)

# Concatenate all the rows into a single DataFrame
if kscerato_data:
    kscerato_df = pd.concat(kscerato_data, ignore_index=True)

    # Save the new DataFrame to a new CSV file
    kscerato_df.to_csv('C:\\Users\\Lazaro B\\Documents\\GitHub\\CSGOProject\\data\\Espionage\\Cabbi\\Cabbitotal.csv', index=False)
