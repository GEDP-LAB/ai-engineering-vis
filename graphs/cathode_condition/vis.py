import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.lines as mlines

import config


def draw_graph(data, y_value='1.8'):
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", config.COLOR_RANGE_NORM[::-1])
    norm = mcolors.Normalize(vmin=data['I/C in Cathode'].min(), vmax=data['I/C in Cathode'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    data = data[data['Pt wt. %'] < 1]

    data = data.sort_values(by='Pt wt. %', ascending=True)

    # Creating the scatter plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        data['Pt wt. %'],
        data[y_value],
        s=data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)']*50,  # Adjust size for visibility
        c=sm.to_rgba(data['I/C in Cathode']),  # Color based on 'Pt wt. %'
        cmap=cmap,
        norm=norm,
        edgecolor='none'
    )

    # Adding color bar for 'Pt wt. %'
    cbar = plt.colorbar(scatter, label='I/C in Cathode')
    cbar.update_normal(sm)
    cbar.set_label('I/C in Cathode', rotation=270, labelpad=15)

    # For linewidth - representing 'Anode Precious Metal Loading'
    legend1 = mlines.Line2D([], [],
                            color='gray', marker='o',
                            markersize=4,
                            label='Lower', linestyle='None')
    legend2 = mlines.Line2D([], [],
                            color='gray',
                            marker='o',
                            markersize=10,
                            label='Higher', linestyle='None')

    # Adding legends to the plot with a title
    plt.legend(handles=[legend1, legend2], loc='upper right', title='I/C in Cathode')

    # Setting labels and title
    plt.xlabel('Cathode Precious Metal Loading (mg cm-2 Pt/Pd)')
    plt.ylabel(f'Y Value ({y_value})')
    plt.title(f'Scatter Plot with Cathode Precious Metal Loading and Y Value ({y_value})')
