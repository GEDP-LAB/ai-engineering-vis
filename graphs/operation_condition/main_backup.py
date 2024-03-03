import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
import numpy as np

# Load the data
df = pd.read_excel('operation_condition.xlsx')

# Prepare the data for visualization
df['Active Area (cm2)'] = pd.to_numeric(df['Active Area (cm2)'], errors='coerce')
df['size'] = (df['Operating Temperature (℃)'] - df['Operating Temperature (℃)'].min()) / (df['Operating Temperature (℃)'].max() - df['Operating Temperature (℃)'].min() + 1)
df['border'] = (df['Anode Pressure (bar)'] - df['Anode Pressure (bar)'].min()) / (df['Anode Pressure (bar)'].max() - df['Anode Pressure (bar)'].min())
df['border_size'] = (df['Cathode Pressure (bar)'] - df['Cathode Pressure (bar)'].min()) / (df['Cathode Pressure (bar)'].max() - df['Cathode Pressure (bar)'].min())

# Create scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df['Active Area (cm2)'], df[1.8],
                      c=df['Flow Rate (Ml/min)'],
                      cmap=plt.cm.plasma,
                      s=100 * df['size'] + 10,
                      edgecolor=plt.cm.viridis(df['border']),
                      linewidths=3 * df['border_size'] + 0.5,
                      alpha=0.6)

# Adding color bar for flow rate
cbar = plt.colorbar(scatter)
cbar.set_label('Flow Rate (Ml/min)')

# Adding labels and title
plt.xlabel('Active Area (cm²)')
plt.ylabel('1.8')
plt.title('Modified Scatter Plot')

# Legends for temperature
temp_sizes = [df['Operating Temperature (℃)'].min(), df['Operating Temperature (℃)'].quantile(0.5), df['Operating Temperature (℃)'].max()]
temp_handles = []
for size in temp_sizes:
    handle = plt.scatter([], [], c='gray', alpha=0.6,
                         s=80 * ((size - df['Operating Temperature (℃)'].min()) / (df['Operating Temperature (℃)'].max() - df['Operating Temperature (℃)'].min()) + 0.1),
                         label=f'{size} ℃')
    temp_handles.append(handle)

# Legends for cathode pressure
cathode_pressures = [df['Cathode Pressure (bar)'].min(), df['Cathode Pressure (bar)'].median(), df['Cathode Pressure (bar)'].max()]
pressure_handles = []
for pressure in cathode_pressures:
    handle = plt.scatter([], [], c='gray', alpha=0.6, edgecolor='black',
                         linewidths=3 * ((pressure - df['Cathode Pressure (bar)'].min()) / (df['Cathode Pressure (bar)'].max() - df['Cathode Pressure (bar)'].min()) + 0.5),
                         label=f'{pressure} bar')
    pressure_handles.append(handle)

# Create a range of colors that will be used in the legend
anode_pressure_range = np.linspace(df['Anode Pressure (bar)'].min(), df['Anode Pressure (bar)'].max(), num=5)
anode_pressure_colors = plt.cm.viridis((anode_pressure_range - df['Anode Pressure (bar)'].min()) / (df['Anode Pressure (bar)'].max() - df['Anode Pressure (bar)'].min()))

# Create legend handles for the anode pressure
anode_pressure_handles = []
for pressure, color in zip(anode_pressure_range, anode_pressure_colors):
    handle = mpatches.Patch(color=color, label=f'{pressure:.2f} bar')
    anode_pressure_handles.append(handle)

# Add the first two legends (for Temperature and Cathode Pressure)
legend1 = plt.legend(handles=temp_handles, title='Temperature Legend', loc='upper right', bbox_to_anchor=(1, 1))
plt.gca().add_artist(legend1)
legend2 = plt.legend(handles=pressure_handles, title='Cathode Pressure Legend', loc='upper right', bbox_to_anchor=(1, 0.85))
plt.gca().add_artist(legend2)

# Add the legend for Anode Pressure (Border Color)
plt.legend(handles=anode_pressure_handles, title='Anode Pressure (Border Color)', loc='upper right', bbox_to_anchor=(1, 0.7))

# Show plot
plt.show()

# save the plot
# plt.savefig('operation_condition.png')