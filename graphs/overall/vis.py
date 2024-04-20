import textwrap

import matplotlib.pyplot as plt
import pandas as pd

import config

def draw_graph(data):
    color_1 = config.COLOR_RANGE_NORM[0]
    color_2 = config.COLOR_RANGE_NORM[len(config.COLOR_RANGE_NORM) // 2]
    color_3 = config.COLOR_RANGE_NORM[-1]

    # Creating the histogram
    plt.hist(data["1.5"], color=color_1, alpha=0.7, bins=30, label='1.5')
    plt.hist(data["1.8"], color=color_2, alpha=0.7, bins=30, label='1.8')
    plt.hist(data["2"], color=color_3, alpha=0.7, bins=30, label='2.0')

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Three Columns')
    plt.legend(title='Performance Curve')
    plt.show()

def draw_feature_correlation_heatmap(data, mcolors=None, sns=None):
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