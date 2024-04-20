import textwrap

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import config


def draw_graph(data, y_value='1.8'):
    # Transforming Anode and Cathode data
    anode_data = data[['Title', 'Anode PTL Type', 'Anode PTL Thickness(㎛)', y_value]].copy()
    # does not keep decimal point
    anode_data['PTL Type'] = [str(int(x)) for x in anode_data['Anode PTL Type']]
    anode_data['PTL Thickness(㎛)'] = pd.to_numeric(anode_data['Anode PTL Thickness(㎛)'])
    anode_data['Anode or Cathode'] = 'Anode'
    anode_data.drop(['Anode PTL Type', 'Anode PTL Thickness(㎛)'], axis=1, inplace=True)

    cathode_data = data[['Title', 'Cathode PTL Type', 'Cathode PTL Thickness(㎛)', y_value]].copy()
    cathode_data['PTL Type'] =  [str(int(x)) for x in cathode_data['Cathode PTL Type']]
    cathode_data['PTL Thickness(㎛)'] = pd.to_numeric(cathode_data['Cathode PTL Thickness(㎛)'])
    cathode_data['Anode or Cathode'] = 'Cathode'
    cathode_data.drop(['Cathode PTL Type', 'Cathode PTL Thickness(㎛)'], axis=1, inplace=True)

    bins = [50, 100, 150, 200, 250, 300, 350, 400]
    labels = ['50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400']
    anode_data['PTL Thickness(㎛)'] = pd.cut(anode_data['PTL Thickness(㎛)'], bins=bins, labels=labels)
    cathode_data['PTL Thickness(㎛)'] = pd.cut(cathode_data['PTL Thickness(㎛)'], bins=bins, labels=labels)

    # Combining Anode and Cathode data
    combined_data = pd.concat([anode_data, cathode_data])

    # Cleaning the 'PTL Type' column and removing NaN values
    combined_data['PTL Type'] = combined_data['PTL Type'].astype(str)
    combined_data = combined_data[combined_data['PTL Type'] != 'nan']


    # Define colors for each 'PTL Type'
    unique_ptl_types = ["0", "1", "2", "3"]
    labels_name = ['Carbon Paper', 'Titanium Fiber Mesh', 'Titanium Gold', 'Carbon Cloth']
    colors = config.COLOR_GROUPS_NORM[0:len(unique_ptl_types)]
    labels_color = [colors[0], colors[1], colors[2], colors[3]]

    # Splitting the scatter plot into two: one for Anode and one for Cathode
    plt.figure(figsize=(15, 6))

    # Plot for Anode
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
    anode_data_only = combined_data[combined_data['Anode or Cathode'] == 'Anode']
    for ptype, ptype_group in anode_data_only.groupby('PTL Type'):
        sns.violinplot(x=ptype_group['PTL Thickness(㎛)'],
                       y=ptype_group[y_value],
                       color=colors[list(unique_ptl_types).index(ptype)],
                       label=f'{ptype}')
    # add legend
    patches = [plt.plot([], [], marker="o", ms=10, ls="", mec=None, color=labels_color[i], label="{:s}".format(labels_name[i]))[0] for i in range(len(labels_name))]
    plt.legend(handles=patches,
               title='PTL Type',
               bbox_to_anchor=(1.05, 1))

    plt.xlabel('PTL Thickness($\mu$m)')
    plt.ylabel(f'Y Value ({y_value})')
    plt.title('Anode: PTL Thickness vs. Y Value')
    plt.grid(True)

    # Plot for Cathode
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    cathode_data_only = combined_data[combined_data['Anode or Cathode'] == 'Cathode']
    for ptype, ptype_group in cathode_data_only.groupby('PTL Type'):
        sns.violinplot(x=ptype_group['PTL Thickness(㎛)'],
                       y=ptype_group[y_value],
                        color=colors[list(unique_ptl_types).index(ptype)],
                        label=f'{ptype}')

    # add legend
    patches = [plt.plot([], [], marker="o", ms=10, ls="", mec=None, color=labels_color[i], label="{:s}".format(labels_name[i]))[0] for i in range(len(labels_name))]
    plt.legend(handles=patches,
               title='PTL Type',
               bbox_to_anchor=(1.05, 1))

    plt.xlabel(r'PTL Thickness($\mu$m)')
    plt.ylabel(f'Y Value ({y_value})')
    plt.title('Cathode: PTL Thickness vs. Y Value')
    plt.grid(True)

def draw_feature_correlation_heatmap(data, mcolors=None):
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
