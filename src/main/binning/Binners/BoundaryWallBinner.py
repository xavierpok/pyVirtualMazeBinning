import numpy as np

from enum import Enum

import Binner

DEFAULT_SIZE = (30,5)
DEFAULT_CENTER = (0,0,0)
WALL_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class BoundaryWallbinner(Binner):
    # center = np.array((np.NAN,np.NAN,np.NAN))
    # size = np.array(DEFAULT_SIZE)
    # bin_cache = np.zeros((0,0,0))


    
    def __init__(self, center = DEFAULT_CENTER, size = DEFAULT_SIZE):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.center = np.array(center)
        self.size = np.array(size)
        
        #make assumption it's a square
        cache_width = size[0] / WALL_BIN_SIZE[0]
        cache_height = size[1] / WALL_BIN_SIZE[1]
        self.bin_cache = np.zeros((cache_width,cache_height,4))
        # for four walls
        
    
    
    def add_to_bin(self, point : tuple(int,int,int)) -> tuple(int,int,int):
        #first, determine which wall the point lands on
        
        point_as_array = np.array(point)
        
        relative_coord = self.center - point_as_array
        
        # There are four walls, two perpendicular to X, two perpendicular to Z
        # If the magnitude of the relative coord is highest in X, must be one of the 2 X-walls
        # and so on for Z
        max_axis = np.argmax(np.abs(relative_coord))
        axis_sign = np.sign(relative_coord[max_axis])
        if axis_sign == 0 :
            print(f"Error encountered with point : {point} with binner {self} (Center at {self.center}), " + 
                  f"relative coord {relative_coord}")
            pass
        
        if max_axis == 0 :
            face = WallFacing.POS_X if axis_sign > 0 else WallFacing.NEG_X
        elif max_axis == 2 :
            face = WallFacing.POS_Z if axis_sign > 0 else WallFacing.NEG_Z
        
        #Now, fit into the wall 
        relevant_axis = max_axis
        pos_on_wall = np.array((relative_coord[relevant_axis],relative_coord[1])) #relevant axis, y
        bin_pos = np.floor(pos_on_wall / WALL_BIN_SIZE)
        self.bin_cache[(bin_pos) + (face.value,)] += 1
        return (bin_pos) + (face.value,)
        
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    
class WallFacing(Enum):
    """Docstring TODO."""
    NEG_X = 0
    NEG_Z = 1
    POS_X = 2
    POS_Z = 3




    
    