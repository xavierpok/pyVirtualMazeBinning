

from .bin_consts import BINNER_TO_BASE_OFFSET, OBJ_TO_BINNER,poster_matcher
from .Binners import Binner
import numpy as np
import pandas as pd

def ravel_bin_num(binner_arr, rel_bin_num_arr : np.array) :
    # bounds can be found via bin_cache of hte respective binner
    # print(rel_bin_num,binner.bin_cache.shape[0],binner)
    get_binner_shape = lambda binner : np.array(binner.bin_cache.shape)
    
    # binner_series = pd.Series(binner_arr)
    # binner_shape_arr =  binner_series.map(get_binner_shape).to_numpy()
    # i have no idea why this doesn't work
    
    # for i in range(len(binner_arr)) :
    #     binner = binner_arr[i]
    #     if i > 1050000:
    #         print(binner,i)
    #     a = binner.bin_cache.shape
    binner_shape_arr = np.array([get_binner_shape(binner) for binner in binner_arr])
    
    return rel_bin_num_arr[:,0] + binner_shape_arr[:,0] * rel_bin_num_arr[:,1] + \
               binner_shape_arr[:,0] * binner_shape_arr[:,1] * rel_bin_num_arr[:,2]

def get_abs_bin(binner_arr, rel_bin_num_arr : np.array):
    binner_as_series = pd.Series(binner_arr)
    base_offset_series = binner_as_series.map(BINNER_TO_BASE_OFFSET)
    base_offset_array = base_offset_series.to_numpy()
    return base_offset_array + ravel_bin_num(binner_arr, rel_bin_num_arr)

# def add_to_bin(obj_name_arr : np.array, hitloc_arr : np.array):
#     if obj_name == "Poster" :
#         binner_to_use = poster_matcher(hitloc)
#     else : 
#         binner_to_use = OBJ_TO_BINNER[obj_name]    
#     return get_abs_bin(binner_to_use,binner_to_use.add_to_bin(hitloc))

    
