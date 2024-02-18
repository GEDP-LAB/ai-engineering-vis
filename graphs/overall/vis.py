import matplotlib.pyplot as plt
import pandas as pd

def draw_graph(data):
    data['size'] = (data['Operating Temperature (℃)'] - data['Operating Temperature (℃)'].min()) / (data['Operating Temperature (℃)'].max() - data['Operating Temperature (℃)'].min() + 1)
    data['border'] = (data['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'] - data['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'].min()) / (data['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'].max() - data['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'].min())
    data['border_size'] = (data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'] - data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) / (data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max() - data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min())

    # Create scatter plot with legend
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(data['Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)'], data[1.8],
                          c=data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'],
                          cmap=plt.cm.plasma,
                          s=100 * data['size'] + 10,
                          edgecolor=plt.cm.viridis(data['border']),
                          linewidths=3 * data['border_size'] + 0.5,
                          alpha=0.6)

    # Adding color bar for Cathode Precious Metal Loading
    cbar = plt.colorbar(scatter)
    cbar.set_label('Cathode Precious Metal Loading (mg cm-2 Pt/Pd)')

    # Adding labels and title
    plt.xlabel('Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)')
    plt.ylabel('1.8')
    plt.title('Modified Scatter Plot with Legend')

    # Legends for temperature and precious metal loading
    temp_sizes = [data['Operating Temperature (℃)'].min(), data['Operating Temperature (℃)'].quantile(0.5), data['Operating Temperature (℃)'].max()]
    for size in temp_sizes:
        plt.scatter([], [], c='gray', alpha=0.6, s=80 * ((size - data['Operating Temperature (℃)'].min()) / (data['Operating Temperature (℃)'].max() - data['Operating Temperature (℃)'].min()) + 0.1),
                    label=f'{size} ℃')

    cathode_pressures = [data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min(), data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].median(), data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max()]
    for pressure in cathode_pressures:
        plt.scatter([], [], c='gray', alpha=0.6, edgecolor='black', linewidths=3 * ((pressure - data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) / (data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max() - data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) + 0.5),
                    label=f'{pressure} mg/cm² Pt/Pd')

    # Positioning the legend
    # plt.legend(title='Legend', loc='upper right', borderaxespad=1)

    # Legends for temperature
    temp_sizes = [data['Operating Temperature (℃)'].min(), data['Operating Temperature (℃)'].quantile(0.5), data['Operating Temperature (℃)'].max()]
    temp_handles = [plt.scatter([], [], c='gray', alpha=0.6, s=80 * ((size - data['Operating Temperature (℃)'].min()) / (data['Operating Temperature (℃)'].max() - data['Operating Temperature (℃)'].min()) + 0.1),
                    label=f'{size} ℃') for size in temp_sizes]
    legend1 = plt.legend(handles=temp_handles, title='Operating Temperature', loc='upper right')
    plt.gca().add_artist(legend1)

    # Legends for cathode precious metal loading
    cathode_pressures = [data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min(), data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].median(), data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max()]
    pressure_handles = [plt.scatter([], [], c='gray', alpha=0.6, edgecolor='black', linewidths=3 * ((pressure - data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) / (data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].max() - data['Cathode Precious Metal Loading (mg cm-2 Pt/Pd)'].min()) + 0.5),
                    label=f'{pressure} mg/cm² Pt/Pd') for pressure in cathode_pressures]
    plt.legend(handles=pressure_handles, title='Cathode Precious Metal Loading', loc='upper right', bbox_to_anchor=(1, 0.85))
