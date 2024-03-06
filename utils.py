import pandas as pd
import config

def get_subset(data, columns):
    subset = data.iloc[:, columns]
    subset = subset.dropna()
    return subset

def read_xlsx_data(path):
    data = pd.read_excel(config.DATA_DIR + path)
    # change columns name to string
    data.columns = data.columns.astype(str)
    y_index = [data.columns.get_loc('1.5'), data.columns.get_loc('1.8'), data.columns.get_loc('2'), 0]
    operation_data = get_subset(data, [1, 2, 3, 4, 5] + y_index)
    anode_data = get_subset(data, [6, 7, 8, 9, 10, 11, 12] + y_index)
    cathode_data = get_subset(data, [13, 14, 15, 16] + y_index)
    membrane_data = get_subset(data, [17, 18, 19] + y_index)
    PTL_data = get_subset(data, [20, 21, 22, 23] + y_index)
    return operation_data, anode_data, cathode_data, membrane_data, PTL_data

def read_csv_data(path):
    data = pd.read_csv(config.DATA_DIR + path)
    # get the number of columns
    y_index = [data.columns.get_loc('1.5'), data.columns.get_loc('1.8'), data.columns.get_loc('2'), 0]
    operation_data = column_rename(get_subset(data, [1, 2, 3, 4, 5] + y_index))
    anode_data = column_rename(get_subset(data, [6, 7, 8, 9, 10, 11, 12] + y_index))
    cathode_data = column_rename(get_subset(data, [13, 14, 15, 16] + y_index))
    membrane_data = column_rename(get_subset(data, [17, 18, 19] + y_index))
    PTL_data = column_rename(get_subset(data, [20, 21, 22, 23] + y_index))
    return operation_data, anode_data, cathode_data, membrane_data, PTL_data

def column_rename(data):
    data.columns = [config.DATA_MAP[data.columns[i]] for i in range(len(data.columns))]
    return data
