from main.IO import reading
from main.binning import bin
import csv
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    savepath = sys.argv[2]

    print(f"Starting on :{path}, saving to {savepath}")
    numerical_vals = reading.read_numerical_vals(path)
    print(numerical_vals)
    obj_names = reading.read_event_type(path)
    print(obj_names)
    with open(savepath, 'w', newline ='') as file :
        writer = csv.writer(file)
        for i in range(numerical_vals.shape[0]) :
            #TODO : vectorise determination of binners
            #TODO : vectorise feeding into binners
            #TODO : vectorise conversion into offset
            
            timestamp = numerical_vals[i,0]
            hitloc = numerical_vals[i,1::]
            # print(timestamp,hitloc)
            name = obj_names[i]
            out_data = (timestamp,bin.add_to_bin(name,hitloc))
            writer.writerow(out_data)
    print("all done")
        