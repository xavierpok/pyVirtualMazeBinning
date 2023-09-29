



from bin_consts import OBJ_TO_BINNER, BINNER_TO_BASE_OFFSET



def ravel_bin_num(binner, rel_bin_num : tuple(int,int,int)) :
    # bounds can be found via bin_cache of hte respective binner
    return rel_bin_num[0] + binner.bin_cache[0] * rel_bin_num[1] + binner.bin_cache[0] * binner.bin_cache[1] * rel_bin_num[2]

def get_abs_bin(binner, rel_bin_num):
    return BINNER_TO_BASE_OFFSET[binner] + ravel_bin_num(rel_bin_num)

def add_to_bin(obj_name : str, hitloc : tuple(int,int,int)):
    binner_to_use = OBJ_TO_BINNER[obj_name]    
    return get_abs_bin(binner_to_use,binner_to_use.add_to_bin(hitloc))

    
