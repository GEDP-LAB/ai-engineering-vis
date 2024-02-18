import pandas as pd
import config

from graphs import draw

def read_data(path):
    data = pd.read_excel(config.DATA_DIR + path)
    data = data.dropna()
    return data


if __name__ == '__main__':
    anode_data = read_data('anode.xlsx')
    cathode_data = read_data('cathode.xlsx')
    membrance_data = read_data('membrance.xlsx')
    operation_data = read_data('operation_condition.xlsx')
    PTL_data = read_data('ptl.xlsx')
    overall_data = read_data('overall.xlsx')

    # draw(config.DATASET.ANODE, anode_data)
    # draw(config.DATASET.CATHODE, cathode_data)
    draw(config.DATASET.MEMBRANE, membrance_data)
    # draw(config.DATASET.OPERATING_CONDITION, operation_data)
    # draw(config.DATASET.PLT, PTL_data)
    # draw(config.DATASET.OVERALL, overall_data)
