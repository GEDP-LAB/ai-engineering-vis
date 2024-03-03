import pandas as pd
import config

from graphs import draw

def get_subset(data, columns):
    subset = data.iloc[:, columns]
    subset = subset.dropna()
    return subset

def read_xlsx_data(path):
    data = pd.read_excel(config.DATA_DIR + path)
    # change columns name to string
    data.columns = data.columns.astype(str)
    y_index = [len(data.columns) - 1, len(data.columns) - 2, len(data.columns) - 3, 0]
    operation_data = get_subset(data, [1, 2, 3, 4, 5] + y_index)
    anode_data = get_subset(data, [6, 7, 8, 9, 10, 11, 12] + y_index)
    cathode_data = get_subset(data, [13, 14, 15, 16] + y_index)
    membrane_data = get_subset(data, [17, 18, 19] + y_index)
    PTL_data = get_subset(data, [20, 21, 22, 23] + y_index)
    return operation_data, anode_data, cathode_data, membrane_data, PTL_data

def column_rename(data):
    data.columns = [config.DATA_MAP[data.columns[i]] for i in range(len(data.columns))]
    return data

def read_csv_data(path):
    data = pd.read_csv(config.DATA_DIR + path)
    # get the number of columns
    y_index = [len(data.columns) - 1, len(data.columns) - 2, len(data.columns) - 3, 0]
    operation_data = column_rename(get_subset(data, [1, 2, 3, 4, 5] + y_index))
    anode_data = column_rename(get_subset(data, [6, 7, 8, 9, 10, 11, 12] + y_index))
    cathode_data = column_rename(get_subset(data, [13, 14, 15, 16] + y_index))
    membrane_data = column_rename(get_subset(data, [17, 18, 19] + y_index))
    PTL_data = column_rename(get_subset(data, [20, 21, 22, 23] + y_index))
    return operation_data, anode_data, cathode_data, membrane_data, PTL_data

if __name__ == '__main__':
    operation_data, anode_data, cathode_data, membrane_data, PTL_data = read_csv_data('train_data_aug_epoch1000_clip.csv')
    # operation_data, anode_data, cathode_data, membrane_data, PTL_data = read_xlsx_data('raw_data2.xlsx')

    draw(config.DATASET.ANODE, anode_data)
    draw(config.DATASET.CATHODE, cathode_data)
    draw(config.DATASET.MEMBRANE, membrane_data)
    draw(config.DATASET.OPERATING_CONDITION, operation_data)
    draw(config.DATASET.PLT, PTL_data)

