#!/usr/bin/env python3

import argparse
import csv


def defuqzecsv(input, output):
    reader = csv.reader(input)
    writer = csv.writer(output, delimiter=',')
    for row in reader:
        # Remove all of the white space
        row = list(map(lambda x: x.strip(), row))
        # Covert ps to seconds
        timestamp = '{0:.12f}'.format(float(row[0]) * 1e-12)
        # Covert the channels to ints
        channels = row[1:]
        writer.writerow([timestamp] + channels)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", nargs=1, type=argparse.FileType('r'), help="input csv exported from the TLA app")
    parser.add_argument("outfile", nargs=1, type=argparse.FileType('w'), help="debroked csv for sigrok")
    args = parser.parse_args()
    defuqzecsv(args.infile[0], args.outfile[0])
