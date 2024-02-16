import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming data_cathode is already loaded and prepared for plotting

data_cathode = pd.read_excel('cathode.xlsx')

# keep data_cathode['I/C in Cathode'] < 15
data_cathode = data_cathode[data_cathode['I/C in Cathode'] < 1]

# Creating the scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    data_cathode['I/C in Cathode'],
    data_cathode[1.8],
    s=data_cathode['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)']*100,  # Adjust size for visibility
    c=data_cathode['Pt wt. %'],  # Color based on 'Pt wt. %'
    cmap='viridis',
    alpha=0.7,
    edgecolor='none'
)

# Adding color bar for 'Pt wt. %'
cbar = plt.colorbar(scatter, label='Pt wt. %')

# Defining custom legend for 'Cathode Precious Metal Loading'
# Specifying ranges for the legend
loading_ranges = [(0.1, 0.2), (0.2, 0.4), (0.4, 0.6)]  # Example ranges in mg cm-2 Pt/Pd
loading_labels = [f'{low}-{high} mg cm-2 Pt/Pd' for low, high in loading_ranges]

# Calculating average size for each range for the legend
average_sizes = [np.mean([low, high]) for low, high in loading_ranges]

# Creating custom legend entries
legend_entries = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                             markerfacecolor='gray', markersize=np.sqrt(size)*10, markeredgewidth=0)
                  for size, label in zip(average_sizes, loading_labels)]

# Adding legends to the plot with a title
plt.legend(handles=legend_entries, title='Metal Loading', loc='upper right')

# Setting labels and title
plt.xlabel('I/C in Cathode')
plt.ylabel('Y Value (1.8)')
plt.title('Scatter Plot with I/C in Cathode Ratio and Y Value (1.8)')

# Show the plot
# plt.show()

# Save the plot as a PNG file
plt.savefig('scatter_plot_cathode.png', bbox_inches='tight')