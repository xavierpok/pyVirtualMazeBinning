import numpy as np

from enum import Enum
from . import Binner

DEFAULT_SIZE = (25,25)
DEFAULT_CENTER = (0,0,0)
CEILING_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class CeilingBinner(Binner.Binner):
    # center = np.array((np.NAN,np.NAN,np.NAN))
    # size = np.array(DEFAULT_SIZE)
    # bin_cache = np.zeros((0,0,0))
    
    def __init__(self, center = DEFAULT_CENTER, size = DEFAULT_SIZE):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.center = np.array(center)
        self.size = np.array(size)
        
        #make assumption it's a square
        cache_width = np.ceil(size[0] / CEILING_BIN_SIZE[0]).astype(int)
        cache_height = np.ceil(size[1] / CEILING_BIN_SIZE[1]).astype(int)
        self.bin_cache = np.zeros((cache_width,cache_height,1))

        
    
    
    def add_to_bin(self, point_arr : np.array) -> tuple:
        # Easy case : Will only ever need to consider x & z
        
        # convention : use x as width, z as height
        
        #reshape needed to allow for broadcasting 
        #axis 0 indexes rows, axis 1 here pulls only x,z coords
        relative_point_arr = (point_arr - self.center.reshape(1,-1))[:,[0,2]]
       
        bin_pos_arr = np.floor(relative_point_arr / np.array(CEILING_BIN_SIZE).reshape(1,-1)).astype(int)
        
        self.bin_cache[bin_pos_arr] += 1
        
        #add additional face col as ceiling has 1 face, i.e. face will always be index 0
        face_col = np.zeros((bin_pos_arr.shape[0],1))
        
        return np.hstack((bin_pos_arr,face_col))
        
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    


