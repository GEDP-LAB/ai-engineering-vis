import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.lines as mlines
import pandas as pd

import config


def draw_graph(data):
    # Ensure 'Membrane Thickness (㎛)' and 'Membrane EW' are numeric
    data['Membrane Thickness (㎛)'] = pd.to_numeric(data['Membrane Thickness (㎛)'], errors='coerce')
    data['Membrane EW'] = pd.to_numeric(data['Membrane EW'], errors='coerce')
    # filter out data['Ultrasonic Spray_0/Brushing_1'] == 0
    # data = data[data['Ultrasonic Spray_0/Brushing_1'] == 1]

    # Create a figure and a set of subplots
    fig, ax = plt.subplots(figsize=(10, 6))

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    cmap2 = mcolors.LinearSegmentedColormap.from_list("custom_cmap2", config.COLOR_RANGE_SUBSET_NORM2)
    norm = mcolors.Normalize(vmin=data['Membrane EW'].min(), vmax=data['Membrane EW'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm2 = plt.cm.ScalarMappable(cmap=cmap2, norm=norm)
    sm.set_array([])
    sm2.set_array([])

    # Creating the scatter plot, the color of the points will be based on Ultrasonic Spray_0/Brushing_1
    # use cmap and sm for Ultrasonic Spray_0/Brushing_1 == 0
    # use cmap2 and sm2 for Ultrasonic Spray_0/Brushing_1 == 1
    subset = data[data['Ultrasonic Spray_0/Brushing_1'] == 0]
    scatter = ax.scatter(subset['Membrane Thickness (㎛)'], subset[1.8],
                         c=subset['Membrane EW'],
                         cmap=cmap,
                         norm=norm,
                         )
    subset = data[data['Ultrasonic Spray_0/Brushing_1'] == 1]
    scatter = ax.scatter(subset['Membrane Thickness (㎛)'], subset[1.8],
                         c=subset['Membrane EW'],
                         cmap=cmap2,
                         norm=norm,
                         )

    # Adding color bar for 'Membrane EW'
    cbar = plt.colorbar(scatter)
    cbar.update_normal(sm)
    cbar.set_label(label='Membrane EW for Ultrasonic Spray', rotation=270, labelpad=15)

    # Adding color bar for 'Membrane EW', add to left of the plot
    cbar = plt.colorbar(scatter)
    cbar.update_normal(sm2)
    cbar.set_label(label='Membrane EW for Brushing', rotation=270, labelpad=15)

    # # Customizing the plot
    ax.set_xlabel(r'Membrane Thickness ($\mu$m)')
    ax.set_ylabel('Y Value')  # Update this label according to your actual Y-axis label
    ax.set_title('Scatter Plot of Membrane Thickness vs. Y Value')
