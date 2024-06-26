import textwrap

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns
import pandas as pd

import config


def draw_graph(data, y_value='1.8'):
    # Ensure 'Membrane Thickness (㎛)' and 'Membrane EW' are numeric
    # only keep 1 decimal point
    data['Membrane Thickness (㎛)'] = pd.to_numeric(data['Membrane Thickness (㎛)'], errors='coerce')
    data['Membrane EW'] = pd.to_numeric(data['Membrane EW'], errors='coerce')

    plt.figure(figsize=(15, 6))

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    norm = mcolors.Normalize(vmin=data['Membrane EW'].min(), vmax=data['Membrane EW'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    bin_counts, edges = pd.cut(data['Membrane Thickness (㎛)'], bins=5, retbins=True)
    edges = [round(x, 1) for x in edges]
    data['Membrane Thickness (㎛)'] = pd.cut(data['Membrane Thickness (㎛)'], bins=edges)

    bin_counts, edges = pd.cut(data['Membrane EW'], bins=3, retbins=True)
    edges = [round(x, 1) for x in edges]
    data['Membrane EW'] = pd.cut(data['Membrane EW'], bins=edges)

    unique_ptl_types = data['Membrane EW'].unique()
    colors = config.COLOR_GROUPS_NORM[0:len(unique_ptl_types)]

    plt.subplot(1, 2, 1)
    subset = data[data['Ultrasonic Spray_0/Brushing_1'] == 0]
    for i, ptl_type in enumerate(unique_ptl_types):
        subsubset = subset[subset['Membrane EW'] == ptl_type]
        sns.violinplot(x='Membrane Thickness (㎛)',
                       y=y_value,
                       label=ptl_type,
                       data=subsubset,
                       palette=colors[i:i+1])
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),
               title='Membrane EW',
               bbox_to_anchor=(1.05, 1))
    plt.xlabel(r'Membrane Thickness ($\mu$m)')
    plt.ylabel(f'Y Value ({y_value})')  # Update this label according to your actual Y-axis label
    plt.title(r'Ultrasonic Spray: Membrane Thickness vs. Y Value')
    plt.grid(True)


    plt.subplot(1, 2, 2)
    subset = data[data['Ultrasonic Spray_0/Brushing_1'] == 1]
    for i, ptl_type in enumerate(unique_ptl_types):
        subsubset = subset[subset['Membrane EW'] == ptl_type]
        sns.violinplot(x='Membrane Thickness (㎛)',
                       y=y_value,
                       label=ptl_type,
                       data=subsubset,
                       palette=colors[i:i+1])

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),
               title='Membrane EW',
               bbox_to_anchor=(1.05, 1))

    plt.xlabel(r'Membrane Thickness ($\mu$m)')
    plt.ylabel(f'Y Value ({y_value})')  # Update this label according to your actual Y-axis label
    plt.title('Brushing: Membrane Thickness vs. Y Value')
    plt.grid(True)


def draw_feature_correlation_heatmap(data):
    plt.figure(figsize=(12, 10))

    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    data.dropna(axis=1, how='all', inplace=True)  # Optional: remove columns that are completely non-numeric

    # Compute the correlation matrix
    correlation_matrix = data.corr()

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_SUBSET_NORM1)
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap=cmap, linewidths=.5, cbar_kws={"shrink": .8},
                     annot_kws={"size": 8})
    ax.set_xticklabels([textwrap.fill(label.get_text(), 15) for label in ax.get_xticklabels()])
    ax.set_yticklabels([textwrap.fill(label.get_text(), 15) for label in ax.get_yticklabels()])
    plt.xlabel('Features', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.tight_layout()  # Adjust layout