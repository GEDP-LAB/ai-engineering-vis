import config
import utils

from graphs import draw

if __name__ == '__main__':
    # operation_data, anode_data, cathode_data, membrane_data, PTL_data, overall_data = utils.read_csv_data('newdata.csv')
    operation_data, anode_data, cathode_data, membrane_data, PTL_data, overall_data = utils.read_xlsx_data('newdata.xlsx')

    y_value = '2'

    draw(config.DATASET.ANODE, anode_data, y_value)
    draw(config.DATASET.CATHODE, cathode_data, y_value)
    draw(config.DATASET.MEMBRANE, membrane_data, y_value)
    draw(config.DATASET.OPERATING_CONDITION, operation_data, y_value)
    draw(config.DATASET.PLT, PTL_data, y_value)
    draw(config.DATASET.OVERALL, overall_data)
