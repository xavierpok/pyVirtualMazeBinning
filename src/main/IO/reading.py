import numpy as np
import pandas as pd
from enum import Enum
import csv


def read_numerical_vals(csv_path : str) -> np.array :
    with open (csv_path, 'r') as file :
        reader = csv.reader(file)
        return np.array([row[0,8,9,10] for row in reader])
 
def read_event_type(csv_path : str) -> np.array :
    with open (csv_path, 'r') as file :
        reader = csv.reader(file)
        return np.array([row[1] for row in reader])

class colNums(Enum) :
    TIME = 1
    OBJ_NAME = 2
    HIT_X = 9
    HIT_Y = 10
    HIT_Z = 11
    