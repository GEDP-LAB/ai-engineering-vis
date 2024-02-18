import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.colors as mcolors

SHOW_PLOT = True
SAVE_PLOT = True


def read_data():
    data = pd.read_excel('anode.xlsx')
    data = data.dropna()
    return data


def draw_graph(data):
    # Convert 'Ionmer catalyst ratio' to numeric values for plotting
    data['Ionmer catalyst ratio'] = pd.to_numeric(data['Ionmer catalyst ratio'], errors='coerce')

    # Create the colormap from specific RGB values
    start_color = np.array([75, 102, 173]) / 255.0  # Normalized RGB for start color
    end_color = np.array([254, 251, 185]) / 255.0  # Normalized RGB for end color
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", [start_color, end_color])
    norm = mcolors.Normalize(vmin=data['Ir wt. %'].min(), vmax=data['Ir wt. %'].max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Renaming the column for easier access
    data = data.rename(columns={'Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)': 'Anode Precious Metal Loading'})

    # Creating the scatter plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        data['Ionmer catalyst ratio'],
        data[1.8],
        c=sm.to_rgba(data['Ir wt. %']),
        cmap=cmap,
        norm=norm,
        edgecolor=['black' if x == 0 else 'red' for x in data['Pure_0/Supported_1']],
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
    edge_color_legend = plt.legend(handles=[legend1, legend2], loc='upper right', title='Edge Color')

    # Add the edge color legend manually to the plot and make room for the next legend
    plt.gca().add_artist(edge_color_legend)

    # For linewidth - representing 'Anode Precious Metal Loading'
    legend3 = mlines.Line2D([], [],
                            color='white', marker='o',
                            markeredgecolor='black',
                            markersize=10,
                            label='Lower Metal Loading', markeredgewidth=1, linestyle='None')
    legend4 = mlines.Line2D([], [],
                            color='white',
                            marker='o',
                            markeredgecolor='black',
                            markersize=10,
                            label='Higher Metal Loading', markeredgewidth=5, linestyle='None')

    # Adjusting the position of the second legend to be below the first one in the upper right
    plt.legend(handles=[legend3, legend4], loc='upper right', bbox_to_anchor=(1, 0.85), title='Metal Loading')

    # Setting labels and title
    plt.xlabel('Ionmer catalyst ratio')
    plt.ylabel('Y Value (1.8)')
    plt.title('Scatter Plot with Ionmer Catalyst Ratio and Y Value (1.8)')

    if SHOW_PLOT:
        plt.show()
    if SAVE_PLOT:
        plt.savefig('scatter_plot.jpg', dpi=300)


if __name__ == '__main__':
    data = read_data()
    draw_graph(data)
