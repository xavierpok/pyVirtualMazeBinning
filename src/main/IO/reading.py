import numpy as np
import pandas as pd
from enum import Enum
import csv


def read_numerical_vals(csv_path : str) -> np.array :
    with open (csv_path, 'r') as file :
        reader = csv.reader(file)
        return np.array([[float(row[1]), float(row[9]), float(row[10]), float(row[11])]
                         for row in reader if '' not in row[8:11]] )
 
def read_event_type(csv_path : str) -> np.array :
    with open (csv_path, 'r') as file :
        reader = csv.reader(file)
        return np.array([row[2] for row in reader if '' not in row[8:11]])

class colNums(Enum) :
    TIME = 1
    OBJ_NAME = 2
    HIT_X = 9
    HIT_Y = 10
    HIT_Z = 11
    