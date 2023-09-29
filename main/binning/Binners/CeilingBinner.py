import numpy as np

from enum import Enum
from main.binning.Binners.Binner import Binner

DEFAULT_SIZE = (25,25)
DEFAULT_CENTER = (0,0,0)
CEILING_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class CeilingBinner(Binner):
    center = np.array((np.NAN,np.NAN,np.NAN))
    size = np.array(DEFAULT_SIZE)
    bin_cache = np.zeros((0,0,0))
    
    def __init__(self, center = DEFAULT_CENTER, size = DEFAULT_SIZE):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.center = np.array(center)
        self.size = np.array(size)
        
        #make assumption it's a square
        cache_width = size[0] / CEILING_BIN_SIZE[0]
        cache_height = size[1] / CEILING_BIN_SIZE[1]
        self.bin_cache = np.zeros((cache_width,cache_height,4))
        # for four walls
        
    
    
    def add_to_bin(self, point : tuple(int,int,int)):
       # Easy case : Will only ever need to consider x & z
       
       # convention : use x as width, z as height
       
       relative_point_floor = (np.array(point) - self.center)[0,2]
       
       self.bin_cache[relative_point_floor] += 1
    
        
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    


