import numpy as np

from enum import Enum
from . import Binner

DEFAULT_SIZE = (5, 3.5, 5)
PILLAR_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class MazeWallBinner(Binner.Binner):
    center = np.array((np.NAN,np.NAN,np.NAN))
    size = np.array(DEFAULT_SIZE)
    bin_cache = np.zeros((0,0,0))
    
    class WallFacing(Enum):
        """Docstring TODO."""
        NEG_X = 0
        NEG_Z = 1
        POS_X = 2
        POS_Z = 3
    
    def __init__(self, center : tuple, size = DEFAULT_SIZE):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.center = np.array(center)
        self.size = np.array(size)
        
        #make assumption it's a square
        cache_width = np.ceil(size[0] / PILLAR_BIN_SIZE[0]).astype(int)
        cache_height = np.ceil(size[1] / PILLAR_BIN_SIZE[1]).astype(int)
        self.bin_cache = np.zeros((cache_width,cache_height,4))
        # for four walls
        
    
    
    def add_to_bin(self, point : tuple) -> tuple:
        #first, determine which wall the point lands on
        
        point_as_array = np.array(point)
        
        relative_coord = point_as_array - self.center
        
        # There are four walls, two perpendicular to X, two perpendicular to Z
        # If the magnitude of the relative coord is highest in X, must be one of the 2 X-walls
        # and so on for Z
        relative_no_y = np.array((relative_coord[0],relative_coord[2]))
        max_axis = np.argmax(np.abs(relative_no_y))
        axis_sign = np.sign(relative_coord[max_axis])
        if axis_sign == 0 :
            print(f"Error encountered with point : {point} with binner {self} (Center at {self.center}), " + 
                  f"relative coord {relative_coord}")
            pass
        
        if max_axis == 0 :
            face = WallFacing.POS_X if axis_sign > 0 else WallFacing.NEG_X
        elif max_axis == 1 :
            face = WallFacing.POS_Z if axis_sign > 0 else WallFacing.NEG_Z
        else : 
            face = WallFacing.POS_X
            print(f"Max axis could not be found in {self}, point was {point_as_array}")
        
        #Now, fit into the wall 
        relevant_axis = max_axis
        pos_on_wall = np.array((relative_no_y[relevant_axis],relative_coord[1])) #relevant axis, y
        pos_to_corner = pos_on_wall.copy()
        pos_to_corner[0] += self.size[0]/2
        bin_pos = np.floor(pos_on_wall / PILLAR_BIN_SIZE).astype(int)
        self.bin_cache[(bin_pos) + (face.value,)] += 1
        return tuple(bin_pos) + (face.value,)
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    




class WallFacing(Enum):
    """Docstring TODO."""
    NEG_X = 0
    NEG_Z = 1
    POS_X = 2
    POS_Z = 3
    