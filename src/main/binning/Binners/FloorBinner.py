import numpy as np

from enum import Enum
from . import Binner

DEFAULT_SIZE = (25,25)
DEFAULT_CENTER = (0,0,0)
FLOOR_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class FloorBinner(Binner.Binner):
    center = np.array((np.NAN,np.NAN,np.NAN))
    size = np.array(DEFAULT_SIZE)
    corner = np.array((np.NAN,np.NAN,np.NAN))
    bin_cache = np.zeros((0,0,0))
    
    def __init__(self, center = DEFAULT_CENTER, size = DEFAULT_SIZE):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.center = np.array(center)
        self.size = np.array(size)
        self.corner = np.array((self.center[0] - (self.size[0]/2) , 0 , self.center[2] - (self.size[1] / 2)))
        
        #make assumption it's a square
        cache_width = np.ceil(size[0] / FLOOR_BIN_SIZE[0]).astype(int)
        cache_height = np.ceil(size[1] / FLOOR_BIN_SIZE[1]).astype(int)
        self.bin_cache = np.zeros((cache_width,cache_height,1))
        # for four walls
        
    
    
    def add_to_bin(self, point : tuple) -> tuple:
       # Easy case : Will only ever need to consider x & z
       
       # convention : use x as width, z as height
       
        relative_point_floor = (np.array(point) - self.corner)[[0,2]]
       
        bin_pos = np.floor(relative_point_floor / FLOOR_BIN_SIZE).astype(int)

        self.bin_cache[bin_pos] += 1
        return tuple(bin_pos) + (0,)
        
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    


