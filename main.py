import pandas as pd
import config

from graphs import draw

def get_subset(data, columns):
    columns.append(0)
    columns.append(24)
    subset = data.iloc[:, columns]
    subset = subset.dropna()
    return subset

def read_xlsx_data(path):
    data = pd.read_excel(config.DATA_DIR + path)
    # operation_data = get_subset(data, [1, 2, 3, 4, 5])
    # anode_data = get_subset(data, [6, 7, 8, 9, 10, 11, 12])
    # cathode_data = get_subset(data, [13, 14, 15, 16])
    # membrane_data = get_subset(data, [17, 18, 19])
    # PTL_data = get_subset(data, [20, 21, 22, 23])
    return data

def read_csv_data(path, title):
    data = pd.read_csv(config.DATA_DIR + path)
    data.columns = title
    operation_data = get_subset(data, [1, 2, 3, 4, 5])
    anode_data = get_subset(data, [6, 7, 8, 9, 10, 11, 12])
    cathode_data = get_subset(data, [13, 14, 15, 16])
    membrane_data = get_subset(data, [17, 18, 19])
    PTL_data = get_subset(data, [20, 21, 22, 23])
    return operation_data, anode_data, cathode_data, membrane_data, PTL_data, data.columns

if __name__ == '__main__':
    anode_data = read_xlsx_data('raw_data2.xlsx')

    # get the title of all the columns
    # put the title into a list
    # title = []
    # for i in range(len(anode_data.columns)):
    #     title.append(anode_data.columns[i])
    #
    # operation_data, anode_data, cathode_data, membrance_data, PTL_data, columns = read_csv_data('train_data_aug_epoch1000_clip.csv', title)
    #
    # for i in range(len(title)):
    #     print(columns[i], "\t", title[i])

    anode_data = read_xlsx_data('anode.xlsx')
    cathode_data = read_xlsx_data('cathode.xlsx')
    membrance_data = read_xlsx_data('membrance.xlsx')
    operation_data = read_xlsx_data('operation_condition.xlsx')
    PTL_data = read_xlsx_data('ptl.xlsx')
    overall_data = read_xlsx_data('overall.xlsx')



    draw(config.DATASET.ANODE, anode_data)
    draw(config.DATASET.CATHODE, cathode_data)
    draw(config.DATASET.MEMBRANE, membrance_data)
    draw(config.DATASET.OPERATING_CONDITION, operation_data)
    draw(config.DATASET.PLT, PTL_data)

