import textwrap

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import matplotlib.patches as mpatches
import numpy as np

import config


def draw_graph(data, y_value='1.8'):
    # Prepare the data for visualization
    data['Active Area (cm2)'] = pd.to_numeric(data['Active Area (cm2)'], errors='coerce')
    data = data[data['Active Area (cm2)'] < 25]
    # data = data[data['Flow Rate (Ml/min)'] < 15]

    data['size'] = (data['Operating Temperature (℃)'] - data['Operating Temperature (℃)'].min()) / (
                data['Operating Temperature (℃)'].max() - data['Operating Temperature (℃)'].min() + 1)
    data['border'] = (data['Anode Pressure (bar)'] - data['Anode Pressure (bar)'].min()) / (
                data['Anode Pressure (bar)'].max() - data['Anode Pressure (bar)'].min())
    data['border_size'] = (data['Cathode Pressure (bar)'] - data['Cathode Pressure (bar)'].min()) / (
                data['Cathode Pressure (bar)'].max() - data['Cathode Pressure (bar)'].min())

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_NORM[::-1])
    # cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    norm = mcolors.Normalize(vmin=data['Active Area (cm2)'].min(), vmax=data['Active Area (cm2)'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    cmap_border = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_PINK_NORM)
    norm_border = mcolors.Normalize(vmin=data['Anode Pressure (bar)'].min(), vmax=data['Anode Pressure (bar)'].max())
    sm_border = plt.cm.ScalarMappable(cmap=cmap_border, norm=norm_border)
    sm_border.set_array([])

    # make the data points with higher 'Anode Pressure' to the front of the plot
    data = data.sort_values(by='Anode Pressure (bar)', ascending=True)

    # Create scatter plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(data['Active Area (cm2)'], data[y_value],
                          c=data['Flow Rate (Ml/min)'],
                          cmap=cmap,
                          s=100 * data['size'] + 10,
                          edgecolor=sm_border.to_rgba(data['Anode Pressure (bar)']),
                          linewidths=3 * data['border_size'] + 0.5,
                          norm=norm)

    # Adding color bar for flow rate
    cbar = plt.colorbar(scatter)
    cbar.update_normal(sm)
    cbar.set_label('Flow Rate (Ml/min)', rotation=270, labelpad=15)


    # Adding labels and title
    plt.xlabel('Active Area (cm²)')
    plt.ylabel(y_value)
    plt.title(f'Active Area vs Y Value ({y_value})')

    # Legends for temperature
    temp_sizes = [data['Operating Temperature (℃)'].min(),
                  data['Operating Temperature (℃)'].max()]
    temp_handles = []
    for size in temp_sizes:
        handle = plt.scatter([], [], c='gray', alpha=0.6,
                             s=80 * ((size - data['Operating Temperature (℃)'].min()) / (
                                         data['Operating Temperature (℃)'].max() - data[
                                     'Operating Temperature (℃)'].min()) + 0.1),
                                label="Lower Temperature" if size == data['Operating Temperature (℃)'].min() else "Higher Temperature")
        temp_handles.append(handle)

    # Legends for cathode pressure
    cathode_pressures = [data['Cathode Pressure (bar)'].min(),
                         data['Cathode Pressure (bar)'].max()]
    pressure_handles = []
    for pressure in cathode_pressures:
        handle = plt.scatter([], [], c='gray', alpha=0.6, edgecolor='black',
                             linewidths=3 * ((pressure - data['Cathode Pressure (bar)'].min()) / (
                                         data['Cathode Pressure (bar)'].max() - data[
                                     'Cathode Pressure (bar)'].min()) + 0.5),
                             label="Lower Cathode Pressure" if pressure == data['Cathode Pressure (bar)'].min() else "Higher Cathode Pressure")
        pressure_handles.append(handle)

    # Create a range of colors that will be used in the legend
    anode_pressure_range = np.linspace(data['Anode Pressure (bar)'].min(), data['Anode Pressure (bar)'].max(), num=5)
    anode_pressure_colors = sm_border.to_rgba(anode_pressure_range)

    # Create legend handles for the anode pressure
    anode_pressure_handles = []
    for pressure, color in zip(anode_pressure_range, anode_pressure_colors):
        handle = mpatches.Patch(color=color, label=f'{pressure:.2f} bar')
        anode_pressure_handles.append(handle)

    # Add the first two legends (for Temperature and Cathode Pressure)
    legend1 = plt.legend(handles=temp_handles, title='Temperature', loc='upper right', bbox_to_anchor=(1, 1))
    plt.gca().add_artist(legend1)
    legend2 = plt.legend(handles=pressure_handles, title='Cathode Pressure Legend', loc='upper right',
                         bbox_to_anchor=(1, 0.88))
    plt.gca().add_artist(legend2)

    # Add the legend for Anode Pressure (Border Color)
    plt.legend(handles=anode_pressure_handles, title='Anode Pressure (Border Color)', loc='upper right',
               bbox_to_anchor=(1, 0.76))

def draw_feature_correlation_heatmap(data, sns=None):
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