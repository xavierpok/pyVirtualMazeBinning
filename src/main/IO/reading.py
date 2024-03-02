from enum import Enum
import csv
import numpy as np

def read_numerical_vals(csv_path: str, colNumEnum: Enum) -> np.array:
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        time_col = colNumEnum.TIME
        return np.array([[float(row[time_col.value]), float(row[colNumEnum.HIT_X.value]),
                          float(row[colNumEnum.HIT_Y.value]), float(row[colNumEnum.HIT_Z.value])]
                         for row in reader if '' not in row[8:11]])

def read_event_type(csv_path: str, colNumEnum : Enum) -> np.array:
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        return np.array([row[colNumEnum.OBJ_NAME.value] for row in reader if '' not in row[8:11]])

class colNumsSingleCast(Enum):
    TIME = 1
    OBJ_NAME = 2
    HIT_X = 9
    HIT_Y = 10
    HIT_Z = 11

class colNumsMulticast(Enum):  # Renamed to follow the same convention
    TIME = 1
    OBJ_NAME = 2
    HIT_X = 3
    HIT_Y = 4
    HIT_Z = 5
