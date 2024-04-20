from matplotlib import pyplot as plt

from .anode_condition import vis as anode_condition
from .cathode_condition import vis as cathode_condition
from .membrane import vis as membrane_condition
from .operation_condition import vis as operation
from .PTL import vis as ptl
from .overall import vis as overall

import config

def draw(dataset, data, y_value='1.8'):
    # copy the data to avoid changing the original data
    data = data.copy()
    if dataset == config.DATASET.ANODE:
        anode_condition.draw_graph(data, y_value)
        anode_condition.draw_feature_correlation_heatmap(data)
        show(dataset)
    elif dataset == config.DATASET.CATHODE:
        cathode_condition.draw_graph(data, y_value)
        cathode_condition.draw_feature_correlation_heatmap(data)
        show(dataset)
    elif dataset == config.DATASET.MEMBRANE:
        membrane_condition.draw_graph(data, y_value)
        # membrane_condition.draw_feature_correlation_heatmap(data)
        show(dataset)
    elif dataset == config.DATASET.OPERATING_CONDITION:
        operation.draw_graph(data, y_value)
        membrane_condition.draw_feature_correlation_heatmap(data)
        show(dataset)
    elif dataset == config.DATASET.PLT:
        ptl.draw_graph(data, y_value)
        membrane_condition.draw_feature_correlation_heatmap(data)
        show(dataset)
    elif dataset == config.DATASET.OVERALL:
        overall.draw_graph(data)
        # membrane_condition.draw_feature_correlation_heatmap(data)
        show(dataset)
    else:
        raise ValueError('Invalid dataset')

def show(dataset):
    output_file_name = dataset.get_name() + '.jpg'
    print('output_file_name:', output_file_name)
    if config.SHOW_PLOT:
        plt.show()
    if config.SAVE_PLOT:
        plt.savefig(config.OUTPUT_DIR + output_file_name, dpi=300)
    plt.close()
