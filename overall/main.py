import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset
df_new = pd.read_excel('overall.xlsx')  # Replace with your actual file path

# Prepare the data for visualization
df_new['size'] = (df_new['Operating Temperature (℃)'] - df_new['Operating Temperature (℃)'].min()) / (df_new['Operating Temperature (℃)'].max() - df_new['Operating Temperature (℃)'].min() + 1)
df_new['border'] = (df_new['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'] - df_new['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'].min()) / (df_new['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'].max() - df_new['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'].min())
df_new['border_size'] = (df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'] - df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) / (df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max() - df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min())

# Create scatter plot with legend
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df_new['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'], df_new[1.8],
                      c=df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'],
                      cmap=plt.cm.plasma,
                      s=100 * df_new['size'] + 10,
                      edgecolor=plt.cm.viridis(df_new['border']),
                      linewidths=3 * df_new['border_size'] + 0.5,
                      alpha=0.6)

# Adding color bar for Cathode Precious Metal Loading
cbar = plt.colorbar(scatter)
cbar.set_label('Cathode Precious Metal Loading (mg cm-2 Pt/Pd)')

# Adding labels and title
plt.xlabel('Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)')
plt.ylabel('1.8')
plt.title('Modified Scatter Plot with Legend')

# Legends for temperature and precious metal loading
temp_sizes = [df_new['Operating Temperature (℃)'].min(), df_new['Operating Temperature (℃)'].quantile(0.5), df_new['Operating Temperature (℃)'].max()]
for size in temp_sizes:
    plt.scatter([], [], c='gray', alpha=0.6, s=80 * ((size - df_new['Operating Temperature (℃)'].min()) / (df_new['Operating Temperature (℃)'].max() - df_new['Operating Temperature (℃)'].min()) + 0.1),
                label=f'{size} ℃')

cathode_pressures = [df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min(), df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].median(), df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max()]
for pressure in cathode_pressures:
    plt.scatter([], [], c='gray', alpha=0.6, edgecolor='black', linewidths=3 * ((pressure - df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) / (df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max() - df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) + 0.5),
                label=f'{pressure} mg/cm² Pt/Pd')

# Positioning the legend
# plt.legend(title='Legend', loc='upper right', borderaxespad=1)

# Legends for temperature
temp_sizes = [df_new['Operating Temperature (℃)'].min(), df_new['Operating Temperature (℃)'].quantile(0.5), df_new['Operating Temperature (℃)'].max()]
temp_handles = [plt.scatter([], [], c='gray', alpha=0.6, s=80 * ((size - df_new['Operating Temperature (℃)'].min()) / (df_new['Operating Temperature (℃)'].max() - df_new['Operating Temperature (℃)'].min()) + 0.1),
                label=f'{size} ℃') for size in temp_sizes]
legend1 = plt.legend(handles=temp_handles, title='Operating Temperature', loc='upper right')
plt.gca().add_artist(legend1)

# Legends for cathode precious metal loading
cathode_pressures = [df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min(), df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].median(), df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max()]
pressure_handles = [plt.scatter([], [], c='gray', alpha=0.6, edgecolor='black', linewidths=3 * ((pressure - df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) / (df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max() - df_new['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) + 0.5),
                label=f'{pressure} mg/cm² Pt/Pd') for pressure in cathode_pressures]
plt.legend(handles=pressure_handles, title='Cathode Precious Metal Loading', loc='upper right', bbox_to_anchor=(1, 0.85))

# Show plot
plt.show()

# Show plot
plt.show()
