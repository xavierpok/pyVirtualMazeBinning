import numpy as np



GLOB_BIN_DEFAULT_SIZE = np.array((0.625,0.625))
class Binner() :
    
    def add_to_bin(self,point : tuple) -> np.array:
        raise NotImplementedError
    def get_all_binCounts(self):
        raise NotImplementedError
    
    