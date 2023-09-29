import numpy as np



class Binner() :
    GLOB_BIN_DEFAULT_SIZE = np.array((0.625,0.625))
    
    def add_to_bin(self,point : tuple(int,int,int)) -> np.array:
        raise NotImplementedError
    def get_all_binCounts(self):
        raise NotImplementedError
    
    