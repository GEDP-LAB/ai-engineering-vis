import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your dataset
data_ptl = pd.read_excel('ptl.xlsx')  # Replace with your file path

# Transforming Anode and Cathode data
anode_data = data_ptl[['Title', 'Anode PTL Type', 'Anode PTL Thickness(㎛)', 1.8]].copy()
anode_data['PTL Type'] = anode_data['Anode PTL Type']
anode_data['PTL Thickness(㎛)'] = anode_data['Anode PTL Thickness(㎛)']
anode_data['Anode or Cathode'] = 'Anode'
anode_data.drop(['Anode PTL Type', 'Anode PTL Thickness(㎛)'], axis=1, inplace=True)

cathode_data = data_ptl[['Title', 'Cathode PTL Type ', 'Cathode PTL Thickness(㎛)', 1.8]].copy()
cathode_data['PTL Type'] = cathode_data['Cathode PTL Type ']
cathode_data['PTL Thickness(㎛)'] = cathode_data['Cathode PTL Thickness(㎛)']
cathode_data['Anode or Cathode'] = 'Cathode'
cathode_data.drop(['Cathode PTL Type ', 'Cathode PTL Thickness(㎛)'], axis=1, inplace=True)

# Combining Anode and Cathode data
combined_data = pd.concat([anode_data, cathode_data])

# Cleaning the 'PTL Type' column
combined_data['PTL Type'] = combined_data['PTL Type'].astype(str)
combined_data = combined_data[~combined_data['PTL Type'].str.isnumeric()]
combined_data = combined_data[combined_data['PTL Type'].notna()]

# Define markers for each 'PTL Type'
unique_ptl_types = combined_data['PTL Type'].unique()
markers = {ptype: marker for ptype, marker in zip(unique_ptl_types, ['o', 's', '^', 'D', 'P', '*'])}

# Colors for 'Anode or Cathode'
colors = {'Anode': 'blue', 'Cathode': 'red'}

# Creating the scatter plot
plt.figure(figsize=(12, 8))

# Iterate over each type and anode/cathode category
for ptype, ptype_group in combined_data.groupby('PTL Type'):
    for anode_cathode, ac_group in ptype_group.groupby('Anode or Cathode'):
        plt.scatter(ac_group['PTL Thickness(㎛)'], ac_group[1.8],
                    marker=markers[ptype], color=colors[anode_cathode],
                    alpha=0.7, label=f'{ptype} - {anode_cathode}')

# Customizing the plot
plt.xlabel(r'PTL Thickness($\mu$m)')
plt.ylabel('Y Value (1.8)')
plt.title('Scatter Plot of PTL Thickness vs. Y Value with Different PTL Types and Anode/Cathode')
plt.legend(title='PTL Type - Anode/Cathode', loc='upper left')
plt.grid(True)
plt.show()
