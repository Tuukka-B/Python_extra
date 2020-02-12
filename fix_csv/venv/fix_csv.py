import argparse
import os
import csv
import sys
import pandas as pd

parser = argparse.ArgumentParser(description='An argument parser for fix_csv to fix csv files (duh).')
parser.add_argument('src', type=str, help='source file for the operation')
parser.add_argument('dst', type=str, help='destination file for the operation')
# bonus 1 starts
parser.add_argument("--in-delimiter", help="the delimiter symbol to replace enclosed with quote-marks")
parser.add_argument("--in-quote", type=str, default="\"", help="the quote symbol to replace enclosed with quote-marks")
# bonus 1 ends
args = parser.parse_args()
"""
if not args.in_delimiter:
    args.in_delimiter = parser.parse_args(['--in_delimiter']).in_delimiter
"""
if args.in_quote != "\"":
    try:
        args.in_quote = args.in_quote.split("\"")[0]
        if len(args.in_quote) > 1:
            print("Incorrect value for in-quote character (max. 1 character allowed), program will now exit.")
            sys.exit(1)
    except IndexError:
        print("Error converting command line parameter in-quote to usable format, program will now exit.")
        sys.exit(1)

if args.in_delimiter:
    args.in_delimiter = args.in_delimiter.split("\"")[0]
    if len(args.in_delimiter) > 1:
        print("Incorrect value for in-delimiter character (max. 1 character allowed), program will now exit.")
        sys.exit(1)
delimiter = ","
quotechar = "\""
with open(os.path.join("./", args.src), "r") as f:
    # bonus 2 starts
    # this replaces user-placed delimiter and quotechar
    args.in_delimiter = csv.Sniffer().sniff(f.read(1024)).delimiter
    f.seek(0)
    args.in_quote = csv.Sniffer().sniff(f.read(1024)).quotechar
    f.seek(0)
    # bonus 2 ends
    read = csv.reader(f, delimiter=args.in_delimiter, quotechar=args.in_quote)

    with open(os.path.join("./", args.dst), "w", newline="") as f2:
        # the csv.writer used to have delimeter and quotechar as kwargs, now it uses defaults
        csv_writer = csv.writer(f2)
        pass

        for row in read:
            # if you want to remove duplicates, use commented code below
            # row = list(dict.fromkeys(row))
            csv_writer.writerow(row)

"""
### testing stuff ###
comp = None
orig = None
with open(os.path.join("./", args.dst), "r") as f2:
    comp = f2.read()

with open(os.path.join("./", args.src), "r") as f:
    orig = f.read()

print("orig:\n", orig)
print("comp:\n", comp)
"""