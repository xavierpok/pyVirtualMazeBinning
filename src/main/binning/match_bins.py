

import pandas as pd
import numpy as np
from . import bin_consts




    
def get_mappers(name_arr : np.array, point_arr : np.array) :
    poster_indices = (name_arr == "Poster") #get boolean arr of special areas
    
    name_series = pd.Series(name_arr)
    out_series = pd.Series(np.zeros(name_arr.shape))
    
    out_series[np.logical_not(poster_indices)] = \
        name_series[np.logical_not(poster_indices)].map(bin_consts.OBJ_TO_BINNER)
    
    # now, handle poster indices
    
    out_series[poster_indices] = find_closest_mazewall(point_arr[poster_indices])

    return out_series.to_numpy()


def find_closest_mazewall(point_arr : np.array) :
    # calc array of distances and do minning

    pillar_centers = np.vstack((pillar.center for pillar in bin_consts.PILLARS))
    
    pillar_centers = pillar_centers.T.reshape((1,3,-1)) 
    #move all the centers into the 3rd dimension
    #so it looks like [x,y,z] stacked in the 3rd dimension
    #do it this way so we can calculate distances in vectorised form
    
    #first, get the raw array
    
    raw_dists = point_arr.reshape((point_arr.shape) + (1,)) - pillar_centers #broadcasting will ensure this is okay
    
    #then, square
    
    squared_dists = np.square(raw_dists)
    
    #then, sum across the rows, which is axis 1.
    
    summed_dists = np.sum(squared_dists,axis=1)
    
    #skip sqrt because for comparison, it's not needed
    
    min_indexes = np.argmin(summed_dists,axis=1) 
    #across the index which indexes pillar type, which was 2, but is now 1 due to summing collapsing a dim
    
    #1-d index array obtained, then just index!
    
    return pd.Series(np.array(bin_consts.PILLARS)[min_indexes])
