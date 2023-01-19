#!/usr/bin/env python3
import csv
import sys
import pandas as pand
import os.path as path

#Reads in CSV's as dataframes with pandas.
#Uses pandas module for easier merging of files without crashing at larger files.
#Will keep all data together and just make new columns for any columns that are different.
#pip install -r  requirements.txt
def main(args):
    
    for filename in args:
        if not path.isfile(filename):
            raise Exception(filename + " does not exist please insure files are real.")

    new_csv = pand.read_csv(args[0], delimiter = ",")
    new_csv['FileName'] = path.basename(args[0])

    for filename in args[1:]:
        temp_csv = pand.read_csv(filename, delimiter = ",")
        temp_csv['FileName'] = path.basename(filename)
        new_csv = pand.concat([new_csv,temp_csv], ignore_index=True)

    
    new_csv.to_csv(sys.stdout, index = False)


if __name__ == '__main__':
    main(sys.argv[1:])

# Input method to generate combined.csv from cmd can remove "> combined.csv" for output to cmd.
# python csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv