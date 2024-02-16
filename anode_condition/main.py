import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Load the data from the Excel file
data_new = pd.read_excel('anode.xlsx')

# Convert 'Ionmer catalyst ratio' to numeric values for plotting
data_new['Ionmer catalyst ratio'] = pd.to_numeric(data_new['Ionmer catalyst ratio'], errors='coerce')

# Renaming the column for easier access
data_new = data_new.rename(columns={'Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)': 'Anode Precious Metal Loading'})

# Creating the scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    data_new['Ionmer catalyst ratio'],
    data_new[1.8],
    c=data_new['Ir wt. %'],
    edgecolor=['black' if x == 0 else 'red' for x in data_new['Pure_0/Supported_1']],
    linewidths=data_new['Anode Precious Metal Loading']
)

# Adding color bar for 'Ir wt. %'
cbar = plt.colorbar(scatter, label='Ir wt. %')

# Creating custom legends
# For edge color (Pure/Supported)
legend1 = mlines.Line2D([], [], color='white', marker='o', markeredgecolor='black', markersize=10, label='Pure (Black Edge)', linestyle='None')
legend2 = mlines.Line2D([], [], color='white', marker='o', markeredgecolor='red', markersize=10, label='Supported (Red Edge)', linestyle='None')
edge_color_legend = plt.legend(handles=[legend1, legend2], loc='upper right', title='Edge Color')


# Add the edge color legend manually to the plot and make room for the next legend
plt.gca().add_artist(edge_color_legend)

# For linewidth - representing 'Anode Precious Metal Loading'
legend3 = mlines.Line2D([], [], color='white', marker='o', markeredgecolor='black', markersize=10, label='Lower Metal Loading', markeredgewidth=1, linestyle='None')
legend4 = mlines.Line2D([], [], color='white', marker='o', markeredgecolor='black', markersize=10, label='Higher Metal Loading', markeredgewidth=5, linestyle='None')

# Adjusting the position of the second legend to be below the first one in the upper right
plt.legend(handles=[legend3, legend4], loc='upper right', bbox_to_anchor=(1, 0.85), title='Metal Loading')


# Setting labels and title
plt.xlabel('Ionmer catalyst ratio')
plt.ylabel('Y Value (1.8)')
plt.title('Scatter Plot with Ionmer Catalyst Ratio and Y Value (1.8)')

# Show the plot
# plt.show()

# Save the plot as a PNG file
plt.savefig('scatter_plot.png', bbox_inches='tight')