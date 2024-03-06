from enum import Enum

import numpy as np

SAVE_PLOT = False
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


DATA_MAP = {
    "Unnamed: 0": "Title",
    "Operating Temperature (℃)": "Operating Temperature (℃)",
    "Cathode Pressure (bar)": "Cathode Pressure (bar)",
    "Anode Pressure (bar)": "Anode Pressure (bar)",
    "Flow Rate (Ml/min)": "Flow Rate (Ml/min)",
    "Active Area (cm2)": "Active Area (cm2)",
    "Ir wt. %": "Ir wt. %",
    "Ru wt.%": "Ru wt.%",
    "O wt. %": "O wt. %",
    "C wt. %": "C wt. %",
    "Pure_0/Supported_1": "Pure_0/Supported_1",
    "Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)": "Anode Precious Metal Loading (mg cm-2 Ir/Ru/Pt/Pd)",
    "Ionmer catalyst ratio": "Ionmer catalyst ratio",
    "Pt wt. %": "Pt wt. %",
    "C wt. %.1": "C wt. %.1",
    "I/C in Cathode": "I/C in Cathode",
    "Cathode Precious Metal Loading (mg cm-2 Pt/Pd)": "Cathode Precious Metal Loading (mg cm-2 Pt/Pd)",
    "Ultrasonic Spray_0/Brushing_1": "Ultrasonic Spray_0/Brushing_1",
    "Membrane Thickness (㎛)": "Membrane Thickness (㎛)",
    "Membrane EW": "Membrane EW",
    "Anode PTL Type": "Anode PTL Type",
    "Anode PTL Thickness(㎛)": "Anode PTL Thickness(㎛)",
    "Cathode PTL Thickness(㎛)": "Cathode PTL Thickness(㎛)",
    "Cathode PTL Type": "Cathode PTL Type",
    "1.5": "1.5",
    "1.8": "1.8",
    "2": "2",
}
