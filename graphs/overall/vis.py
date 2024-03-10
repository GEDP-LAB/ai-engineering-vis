import matplotlib.pyplot as plt

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
