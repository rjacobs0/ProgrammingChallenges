#!/usr/bin/env python3
import csv
import sys
import pandas as pand
import os.path as path

#Can be used for smaller csv files but crashes with large files
#First attempt and preffered method for smaller files.
#combine files into one csv.
def combine_file(writer, reader, filename, testLine):
    firstLine = next(reader)

    #Verify that new csv has same heading as previous if not make a new heading for the csv.
    #Will allow for better understanding of data if new csv has new column.
    if firstLine != testLine:
        writer.writerow(firstLine+["filename"])
    for row in reader:
        if row:
            #Could be expanded to confirm all data points are filled
            #and not write any line that is missing information.
            #if row[0]:
                writer.writerow(
                    row+[filename]
                )
    return firstLine

#read in CSV's and set up writer to stdout.
def main(args):
    outwriter = csv.writer(sys.stdout, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
    testLine = ""
    for filename in args:
        if not path.isfile(filename):
            raise Exception(filename + " does not exist please insure files are real.")

    for filename in args:
        with open(filename, 'r') as csvfile:
            testLine = combine_file(
                outwriter,
                csv.reader(csvfile, delimiter=','),
                path.basename(filename),
                testLine
            )

if __name__ == '__main__':
    main(sys.argv[1:])

# Input method to generate combined.csv from cmd can remove "> combined.csv" for output to cmd.
# python csv-combinerSmaller.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv