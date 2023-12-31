from main.IO import reading
from main.binning import bin

import csv
from main.binning.match_bins import get_mappers,apply_binners
import numpy as np
import sys
import os
if __name__ == "__main__":
    path = sys.argv[1]
    # path = r'C:\Users\Xavier\Documents\GitHub\csvDiffs\unityfile_eyelinkFix.csv'
    if len(sys.argv) >= 3 :
        savepath = sys.argv[2]
    else :
        # path_basename = f"{os.path.splitext(os.path.basename(path))[0]}"
        savepath = os.path.join(os.path.dirname(path),f"binData.csv")

    print(f"Starting on :{path}, saving to {savepath}")
    numerical_vals = reading.read_numerical_vals(path) #reading slow as not vectorised
    # print(numerical_vals)
    hitlocs = numerical_vals[:,1::]
    timestamps = numerical_vals[:,0]
    obj_names = reading.read_event_type(path) #reading slow as not vectorised
    # print(obj_names)
    mappers = get_mappers(obj_names,hitlocs)
    print("Got mappers successfully")
    # print(mappers)
    # print(mappers[mappers == np.nan])
    rel_bin_arr = apply_binners(mappers,hitlocs)
    print("Applied binners successfully")
    abs_bin_arr = bin.get_abs_bin(mappers, rel_bin_arr) # SLOW BECAUSE I HAVEN'T FIGURED OUT HOW TO VECTORISE THIS FULLY
    print("Converted relative to abs bin successfully")
    save_arr = np.hstack((timestamps.reshape(-1,1),abs_bin_arr.reshape(-1,1)))
    np.savetxt(savepath,save_arr,fmt='%d',delimiter=',')
    # with open(savepath, 'w', newline ='') as file :
    #     # writer = csv.writer(file)
    #     for i in range(numerical_vals.shape[0]) :
    #         #TODO : vectorise determination of binners DONE
    #         #TODO : modify binners to be vectorised DONE
    #         #TODO : vectorise feeding into binners DONE
    #         #TODO : vectorise conversion into offset DONE
    #         #TODO : check feeding into binners to make sure the output is in right format
    #         #TODO : check conversion into offset to make sure format agrees
            
    #         timestamp = numerical_vals[i,0]
    #         hitloc = numerical_vals[i,1::]
    #         # print(timestamp,hitloc)
    #         name = obj_names[i]
    #         out_data = (timestamp,bin.add_to_bin(name,hitloc))
    #         writer.writerow(out_data)
    print("all done")
    print(np.max(abs_bin_arr))
        