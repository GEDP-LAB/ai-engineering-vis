import config
import utils

from graphs import draw

if __name__ == '__main__':
    # operation_data, anode_data, cathode_data, membrane_data, PTL_data = utils.read_csv_data('train_data_aug_epoch1000_clip.csv')
    operation_data, anode_data, cathode_data, membrane_data, PTL_data = utils.read_xlsx_data('newdata.xlsx')

    draw(config.DATASET.ANODE, anode_data)
    draw(config.DATASET.CATHODE, cathode_data)
    draw(config.DATASET.MEMBRANE, membrane_data)
    draw(config.DATASET.OPERATING_CONDITION, operation_data)
    draw(config.DATASET.PLT, PTL_data)

