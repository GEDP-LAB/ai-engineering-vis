import matplotlib.pyplot as plt
import pandas as pd

data_raw = pd.read_excel('membrance.xlsx')

# Ensure 'Membrane Thickness (㎛)' and 'Membrane EW' are numeric
data_raw['Membrane Thickness (㎛)'] = pd.to_numeric(data_raw['Membrane Thickness (㎛)'], errors='coerce')
data_raw['Membrane EW'] = pd.to_numeric(data_raw['Membrane EW'], errors='coerce')

# Define border for different categories in 'Ultrasonic Spray_0/Brushing_1'
# 0 for Ultrasonic Spray, 1 for Brushing
# Ultrasonic Spray will have a red border, Brushing will have a no border
marker_properties = {
    0: {'marker': 'o', 'edgecolor': 'red', 'linewidth': 1},  # Red border for Ultrasonic Spray
    1: {'marker': 's', 'edgecolor': 'none', 'linewidth': 0}  # No border for Brushing
}

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Normalize 'Membrane EW' for color mapping
norm = plt.Normalize(data_raw['Membrane EW'].min(), data_raw['Membrane EW'].max())
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])

# Plot each category with its respective marker and border properties
for category, props in marker_properties.items():
    subset = data_raw[data_raw['Ultrasonic Spray_0/Brushing_1'] == category]
    scatter = ax.scatter(subset['Membrane Thickness (㎛)'], subset[1.8],  # Replace 'Your Y-Axis Column Name' with the correct column name
                label=f'{"Ultrasonic Spray" if category == 0 else "Brushing"}',
                # marker=props['marker'],
                c=subset['Membrane EW'],
                cmap="viridis",
                norm=norm,
                edgecolors=props['edgecolor'],
                linewidths=props['linewidth'])

# Adding color bar with explicit reference to the Axes
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Membrane EW')

# Customizing the plot
ax.set_xlabel(r'Membrane Thickness ($\mu$m)')
ax.set_ylabel('Y Value')  # Update this label according to your actual Y-axis label
ax.set_title('Scatter Plot of Membrane Thickness vs. Y Value')
ax.legend(title='Application Method')

# plt.show()

# Save the plot as a PNG file
plt.savefig('scatter_plot_membrane.png', bbox_inches='tight')