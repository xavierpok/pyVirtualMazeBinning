import numpy as np

from enum import Enum

from . import Binner

DEFAULT_SIZE = (30,5)
DEFAULT_CENTER = (0,0,0)
WALL_BIN_SIZE = Binner.GLOB_BIN_DEFAULT_SIZE # axis-specific, & height
class BoundaryWallBinner(Binner.Binner):
    # center = np.array((np.NAN,np.NAN,np.NAN))
    # size = np.array(DEFAULT_SIZE)
    # bin_cache = np.zeros((0,0,0))


    
    def __init__(self, center = DEFAULT_CENTER, size = DEFAULT_SIZE):
        #ASSUME IT'S A SQUARE FOR NOW FOR SIMPLICITY
        self.center = np.array(center)
        self.size = np.array(size)
        
        #make assumption it's a square
        cache_width = np.ceil(size[0] / WALL_BIN_SIZE[0]).astype(int)
        cache_height = np.ceil(size[1] / WALL_BIN_SIZE[1]).astype(int)
        self.bin_cache = np.zeros((cache_width,cache_height,4))
        # for four walls
        
    
    
    def add_to_bin(self, point_arr : np.array) -> tuple:
        #first, determine which wall the point lands on
        

        

        relative_point_arr = (point_arr - self.center)
        # There are four walls, two perpendicular to X, two perpendicular to Z
        # If the magnitude of the relative coord is highest in X, must be one of the 2 X-walls
        # and so on for Z
        relative_no_y = relative_point_arr[:,[0,2]]
        max_axis = np.argmax(np.abs(relative_no_y),axis=1)
        relative_no_y_maxes = np.max(np.abs(relative_no_y),axis=1)
        axis_sign = np.sign(relative_no_y_maxes)
        if np.any(axis_sign) == 0 :
            print(f"Error encountered with point(s) : indices {axis_sign[axis_sign == 0]} with binner {self}" +
                f"(Center at {self.center})," + 
                  f"relative coord(s) {relative_point_arr[axis_sign == 0]}")
            
        face_arr = np.zeros((relative_point_arr.shape[0],1))
        face_arr[np.logical_and(max_axis == 0, axis_sign > 0)] = WallFacing.POS_X.value
        face_arr[np.logical_and(max_axis == 0, axis_sign <= 0)] = WallFacing.NEG_X.value
        face_arr[np.logical_and(max_axis == 1, axis_sign > 0)] = WallFacing.POS_Z.value
        face_arr[np.logical_and(max_axis == 1, axis_sign <= 0)] = WallFacing.NEG_Z.value

        
        #Now, fit into the wall 

        pos_on_wall = np.hstack((relative_no_y_maxes.reshape(-1,1),relative_point_arr[:,1].reshape(-1,1)))
        #make the pos a vertical stack of (relavant_axis,y)
        
        
        pos_to_corner = pos_on_wall.copy()
        pos_to_corner[:,0] += self.size[0]/2
        #add to be wrt to corner
        bin_pos = np.floor(pos_to_corner / WALL_BIN_SIZE).astype(int)
        bin_and_face_pos = np.hstack((bin_pos,face_arr))
        # self.bin_cache[bin_and_face_pos] += 1
        return bin_and_face_pos
        
        
    def get_all_binCounts(self):
        return self.bin_cache.ravel(order='C')
        
    
class WallFacing(Enum):
    """Docstring TODO."""
    NEG_X = 0
    NEG_Z = 1
    POS_X = 2
    POS_Z = 3




    
    