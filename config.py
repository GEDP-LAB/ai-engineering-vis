from enum import Enum

import numpy as np

SAVE_PLOT = True
SHOW_PLOT = True
DATA_DIR = './data/'
OUTPUT_DIR = './output/'
# COLOR_RANGE = np.array([
#     np.array([75, 102, 173]),
#     np.array([98, 190, 166]),
#     np.array([205, 234, 157]),
#     np.array([254, 251, 185]),
#     np.array([253, 186, 107]),
#     np.array([235, 96, 70]),
#     np.array([163, 6, 67]),
# ])

COLOR_RANGE = np.array([
    np.array([231, 98, 84]),
    np.array([239, 138, 71]),
    np.array([247, 170, 88]),
    np.array([255, 208, 111]),
    np.array([255, 230, 183]),

    np.array([170, 220, 224]),
    np.array([114, 188, 213]),
    np.array([82, 143, 173]),
    np.array([55, 103, 149]),
    np.array([30, 70, 110]),
])

COLOR_RANGE_PINK = np.array([
    # np.array([251, 228, 216]),
    # np.array([223, 182, 178]),
    # np.array([133, 79, 108]),
    # np.array([82, 43, 91]),
    # np.array([43, 18, 76]),
    np.array([242, 227, 231]),
    np.array([178, 68, 107]),

])

COLOR_BLACK = np.array([0, 0, 0])

COLOR_RANGE_SUBSET2 = COLOR_RANGE[0:4][::-1]
COLOR_RANGE_SUBSET1 = COLOR_RANGE[5:9]
COLOR_GROUPS = [COLOR_RANGE[9], COLOR_RANGE[6], COLOR_RANGE[4], COLOR_RANGE[0]]

COLOR_RANGE_NORM = COLOR_RANGE / 255.0
COLOR_RANGE_SUBSET_NORM2 = COLOR_RANGE_NORM[0:4][::-1]
COLOR_RANGE_SUBSET_NORM1 = COLOR_RANGE_NORM[5:9]
COLOR_GROUPS_NORM = [COLOR_RANGE_NORM[9], COLOR_RANGE_NORM[6], COLOR_RANGE_NORM[4], COLOR_RANGE_NORM[0]]
COLOR_RANGE_PINK_NORM = COLOR_RANGE_PINK / 255.0
COLOR_BLACK_NORM = COLOR_BLACK / 255.0

class DATASET(Enum):
    ANODE = "anode",
    CATHODE = "cathode",
    MEMBRANE = "membrane"
    OPERATING_CONDITION = "operating_condition"
    PLT = "plt"
    OVERALL = "overall"

    def get_name(self):
        return self.value[0]
