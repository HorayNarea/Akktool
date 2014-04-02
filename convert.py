import csv
import sys


inputfile = sys.argv[1]
with open(inputfile, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        dataset = [row[3], row[2], row[1], row[0], row[4], row[5], row[6], row[7], row[8], row[9], '0', row[10]]
        print ','.join(dataset)

# output csv-structure
#MemberID, firstname, middlename, lastname, birthdate, address, city, zipcode, organisation, haspaid, debt, akk
