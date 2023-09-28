import numpy as np
import pandas as pd
from enum import Enum
import csv


def read_relevant_cols(csv_path : str) -> np.array :
    return np.genfromtxt(csv_path,usecols = (colNums.TIME, colNums.OBJ_NAME,
                                            colNums.HIT_X, colNums.HIT_Y,
                                            colNums.HIT_Z),delimiter = ',' ,filling_values = np.nan)
    
def read_event_type(csv_path : str) -> list :
    with open (csv_path, 'r') as file :
        reader = csv.reader(file)
        return list([row[0] for row in reader])

class colNums(Enum) :
    TIME = 1
    OBJ_NAME = 2
    HIT_X = 9
    HIT_Y = 10
    HIT_Z = 11
    