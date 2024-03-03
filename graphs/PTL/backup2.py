import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def draw_graph(data):
    # Transforming Anode and Cathode data
    anode_data = data[['Title', 'Anode PTL Type', 'Anode PTL Thickness(㎛)', 1.8]].copy()
    anode_data['PTL Type'] = anode_data['Anode PTL Type']
    anode_data['PTL Thickness(㎛)'] = anode_data['Anode PTL Thickness(㎛)']
    anode_data['Anode or Cathode'] = 'Anode'
    anode_data.drop(['Anode PTL Type', 'Anode PTL Thickness(㎛)'], axis=1, inplace=True)

    cathode_data = data[['Title', 'Cathode PTL Type ', 'Cathode PTL Thickness(㎛)', 1.8]].copy()
    cathode_data['PTL Type'] = cathode_data['Cathode PTL Type ']
    cathode_data['PTL Thickness(㎛)'] = cathode_data['Cathode PTL Thickness(㎛)']
    cathode_data['Anode or Cathode'] = 'Cathode'
    cathode_data.drop(['Cathode PTL Type ', 'Cathode PTL Thickness(㎛)'], axis=1, inplace=True)

    # Combining Anode and Cathode data
    combined_data = pd.concat([anode_data, cathode_data])

    # Cleaning the 'PTL Type' column and removing NaN values
    combined_data['PTL Type'] = combined_data['PTL Type'].astype(str)
    combined_data = combined_data[~combined_data['PTL Type'].str.isnumeric()]
    combined_data = combined_data[combined_data['PTL Type'] != 'nan']

    # Define colors for each 'PTL Type'
    unique_ptl_types = combined_data['PTL Type'].unique()
    colors = sns.color_palette('husl', len(unique_ptl_types))

    # Splitting the scatter plot into two: one for Anode and one for Cathode
    plt.figure(figsize=(15, 6))

    # Plot for Anode
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
    anode_data_only = combined_data[combined_data['Anode or Cathode'] == 'Anode']
    for ptype, ptype_group in anode_data_only.groupby('PTL Type'):
        # plt.scatter(ptype_group['PTL Thickness(㎛)'],
        #             ptype_group[1.8],
        #             color=colors[list(unique_ptl_types).index(ptype)],
        #             label=f'{ptype}', marker='o')
        # draw volin plot
        sns.violinplot(x=ptype_group['PTL Thickness(㎛)'],
                       y=ptype_group[1.8],
                       color=colors[list(unique_ptl_types).index(ptype)],
                       label=f'{ptype}')

    plt.xlabel('PTL Thickness($\mu$m)')
    plt.ylabel('Y Value (1.8)')
    plt.title('Anode: PTL Thickness vs. Y Value')
    # plt.legend(title='PTL Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Plot for Cathode
    # plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    # cathode_data_only = combined_data[combined_data['Anode or Cathode'] == 'Cathode']
    # for ptype, ptype_group in cathode_data_only.groupby('PTL Type'):
    #     plt.scatter(ptype_group['PTL Thickness(㎛)'], ptype_group[1.8],
    #                 color=colors[list(unique_ptl_types).index(ptype)],
    #                 alpha=0.7, label=f'{ptype}', marker='o')

    plt.xlabel(r'PTL Thickness($\mu$m)')
    plt.ylabel('Y Value (1.8)')
    plt.title('Cathode: PTL Thickness vs. Y Value')
    plt.legend(title='PTL Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
