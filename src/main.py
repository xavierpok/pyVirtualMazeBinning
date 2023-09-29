from main.IO import reading
from main.binning import bin
import csv

if __name__ == "__main__":
    savepath = r"C:\Users\Xavier\Documents\GitHub\csvDiffs\bins.csv"
    path = r"C:\Users\Xavier\Documents\GitHub\csvDiffs\unityfile_eyelinkFix.csv"
    numerical_vals = reading.read_numerical_vals(path)
    obj_names = reading.read_event_type(path)
    with open(savepath, 'w', newline ='') as file :
        writer = csv.writer(file)
        for i in len(numerical_vals) :
            timestamp = numerical_vals[i,0]
            hitloc = numerical_vals[1::]
            name = obj_names[i]
            out_data = (timestamp,bin.add_to_bin(name,hitloc))
            writer.writerow(out_data)
    print("all done")
        