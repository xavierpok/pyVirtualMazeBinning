from main.IO import reading
from main.binning import bin

import csv
from main.binning.match_bins import get_mappers,apply_binners
import numpy as np
if __name__ == "__main__":
    path = "src\test_data\bintocoords.csv"
    savepath =" src\test_data\results.csv"
    errorpath = "src\test_data\errors.csv"
    print(f"Starting test on : \n{path},\n saving to {savepath}")
    numerical_vals = np.loadtxt(path,usecols=[0,1,2,3],skiprows=1,delimiter=',')
    print(numerical_vals)
    hitlocs = numerical_vals[:,1::]
    timestamps = numerical_vals[:,0]
    obj_names = np.loadtxt(path,usecols = (4,),skiprows=1,delimiter=',',dtype=str)
    print(obj_names)
    mappers = get_mappers(obj_names,hitlocs)
    print("Got mappers successfully")
    # print(mappers)
    # print(mappers[mappers == np.nan])
    rel_bin_arr = apply_binners(mappers,hitlocs)
    print("Applied binners successfully")
    abs_bin_arr = bin.get_abs_bin(mappers, rel_bin_arr) # SLOW BECAUSE I HAVEN'T FIGURED OUT HOW TO VECTORISE THIS FULLY
    print("Converted relative to abs bin successfully")
    save_arr = np.hstack((timestamps.reshape(-1,1),abs_bin_arr.reshape(-1,1)))
    np.savetxt(savepath,save_arr,delimiter=',',fmt='%d')
    
    if (np.any(save_arr[:,0] != save_arr[:,1])) :
        print(f"NOTE : ERROR IN OUTPUT. Saved to {errorpath}")
        np.savetxt(errorpath,save_arr[save_arr[:,0] != save_arr[:,1],:])
    else : 
        print(f"Tested, no discrepancies.")
        

    print("all done")
        