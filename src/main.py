from main.IO import reading
from main.binning import bin

import csv
from main.binning.match_bins import get_mappers

if __name__ == "__main__":
    path = r"C:\Users\Xavier\Documents\GitHub\csvDiffs\unityfile_eyelinkFix.csv"
    savepath = r"C:\Users\Xavier\Documents\GitHub\csvDiffs\bins_2.csv"
    print(f"Starting on :{path}, saving to {savepath}")
    numerical_vals = reading.read_numerical_vals(path)
    print(numerical_vals)
    hitlocs = numerical_vals[:,1::]
    obj_names = reading.read_event_type(path)
    print(obj_names)
    with open(savepath, 'w', newline ='') as file :
        writer = csv.writer(file)
        mappers = get_mappers(obj_names,hitlocs)
        print("Got mappers successfully")
        for i in range(numerical_vals.shape[0]) :
            #TODO : vectorise determination of binners DONE
            #TODO : vectorise feeding into binners
            #TODO : vectorise conversion into offset
            
            timestamp = numerical_vals[i,0]
            hitloc = numerical_vals[i,1::]
            # print(timestamp,hitloc)
            name = obj_names[i]
            out_data = (timestamp,bin.add_to_bin(name,hitloc))
            writer.writerow(out_data)
    print("all done")
        