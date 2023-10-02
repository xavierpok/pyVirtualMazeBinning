import numpy as np

from enum import Enum

from src.main.binning.Binners.MazeWallBinner import MazeWallBinner
from . import Binner

DEFAULT_SIZE = (25,25)
DEFAULT_CENTER = (0,0,0)
CEILING_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class PosterBinner(Binner.Binner):

    
    def __init__(self, mazewall : MazeWallBinner):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.mazewall = mazewall
        self.center = mazewall.center
        self.size = mazewall.size
        
        self.bin_cache = mazewall.bin_cache

        
    
    
    def add_to_bin(self, point : tuple) -> tuple:
        # Easy case : Will only ever need to consider x & z
        
        # convention : use x as width, z as height
        

        return self.mazewall.add_to_bin(point)
        
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    


