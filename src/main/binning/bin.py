

from .bin_consts import BINNER_TO_BASE_OFFSET, OBJ_TO_BINNER,poster_matcher



def ravel_bin_num(binner, rel_bin_num : tuple) :
    # bounds can be found via bin_cache of hte respective binner
    print(rel_bin_num,binner.bin_cache.shape[0],binner)
    return rel_bin_num[0] + binner.bin_cache.shape[0] * rel_bin_num[1] + \
                binner.bin_cache.shape[0] * binner.bin_cache.shape[1] * rel_bin_num[2]

def get_abs_bin(binner, rel_bin_num):
    return BINNER_TO_BASE_OFFSET[binner] + ravel_bin_num(binner, rel_bin_num)

def add_to_bin(obj_name : str, hitloc : tuple):
    if obj_name == "Poster" :
        binner_to_use = poster_matcher(hitloc)
    else : 
        binner_to_use = OBJ_TO_BINNER[obj_name]    
    return get_abs_bin(binner_to_use,binner_to_use.add_to_bin(hitloc))

    
