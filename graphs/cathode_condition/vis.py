import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

import config


# keep data['I/C in Cathode'] < 15
# data = data[data['I/C in Cathode'] < 1]

def draw_graph(data):
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    norm = mcolors.Normalize(vmin=data['Pt wt. %'].min(), vmax=data['Pt wt. %'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    data = data.sort_values(by='Pt wt. %', ascending=True)

    # Creating the scatter plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        data['I/C in Cathode'],
        data[1.8],
        s=data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)']*50,  # Adjust size for visibility
        c=sm.to_rgba(data['Pt wt. %']),  # Color based on 'Pt wt. %'
        cmap=cmap,
        norm=norm,
        edgecolor='none'
    )

    # Adding color bar for 'Pt wt. %'
    cbar = plt.colorbar(scatter, label='Pt wt. %')
    cbar.update_normal(sm)


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
