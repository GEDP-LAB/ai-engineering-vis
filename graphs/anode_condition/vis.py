import textwrap

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
import seaborn as sns

import config


def draw_graph(data, y_value='1.8'):
    # Convert 'Ionmer catalyst ratio' to numeric values for plotting
    data['Ionmer catalyst ratio'] = pd.to_numeric(data['Ionmer catalyst ratio'], errors='coerce')

    # Create the colormap from specific RGB values
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    norm = mcolors.Normalize(vmin=data['Ir wt. %'].min(), vmax=data['Ir wt. %'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Renaming the column for easier access
    data = data.rename(columns={'Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)': 'Anode Precious Metal Loading'})

    data = data.sort_values(by='Pure_0/Supported_1', ascending=True)

    # Creating the scatter plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        data['Ionmer catalyst ratio'],
        data[y_value],
        c=sm.to_rgba(data['Ir wt. %']),
        cmap=cmap,
        norm=norm,
        edgecolor=[config.COLOR_BLACK_NORM if x == 0 else config.COLOR_RANGE_NORM[-1] for x in data['Pure_0/Supported_1']],
        linewidths=data['Anode Precious Metal Loading']
    )

    # Adding color bar for 'Ir wt. %'
    cbar = plt.colorbar(scatter, label='Ir wt. %')
    cbar.update_normal(sm)
    cbar.set_label('Ir wt. %', rotation=270, labelpad=15)

    # Creating custom legends
    # For edge color (Pure/Supported)
    legend1 = mlines.Line2D([], [],
                            color='white',
                            marker='o',
                            markeredgecolor='black',
                            markersize=10, label='Pure (Black Edge)', linestyle='None')
    legend2 = mlines.Line2D([], [],
                            color='white',
                            marker='o',
                            markeredgecolor='red',
                            markersize=10,
                            label='Supported (Red Edge)', linestyle='None')
    edge_color_legend = plt.legend(handles=[legend1, legend2], loc='upper right', title='Pure or Supported')

    # Add the edge color legend manually to the plot and make room for the next legend
    plt.gca().add_artist(edge_color_legend)

    # For linewidth - representing 'Anode Precious Metal Loading'
    legend3 = mlines.Line2D([], [],
                            color='white', marker='o',
                            markeredgecolor='black',
                            markersize=10,
                            label='Lower', markeredgewidth=1, linestyle='None')
    legend4 = mlines.Line2D([], [],
                            color='white',
                            marker='o',
                            markeredgecolor='black',
                            markersize=10,
                            label='Higher', markeredgewidth=5, linestyle='None')

    # Adjusting the position of the second legend to be below the first one in the upper right
    plt.legend(handles=[legend3, legend4], loc='upper right', bbox_to_anchor=(1, 0.85), title='Metal Loading')

    # Setting labels and title
    plt.xlabel('Ionmer catalyst ratio (v/$m^2$)')
    plt.ylabel(f'Y Value ({y_value})')
    plt.title(f'Scatter Plot with Ionmer Catalyst Ratio and Y Value ({y_value})')


def draw_feature_correlation_heatmap(data):
    plt.figure(figsize=(12, 10))
    data_numeric = data.apply(pd.to_numeric, errors='coerce')
    data_numeric = data_numeric.select_dtypes(include=[np.number])
    correlation_matrix = data_numeric.corr()

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap=cmap, linewidths=.5, cbar_kws={"shrink": .8}, annot_kws={"size": 8})
    ax.set_xticklabels([textwrap.fill(label.get_text(), 15) for label in ax.get_xticklabels()])
    ax.set_yticklabels([textwrap.fill(label.get_text(), 15) for label in ax.get_yticklabels()])
    plt.xlabel('Features', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.tight_layout()  # Adjust layout