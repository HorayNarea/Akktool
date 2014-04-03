import csv
import sys


if len(sys.argv) < 2:
    print('Usage:')
    print('\t python ' + sys.argv[0] + ' /path/to/csvfile')
    print('or:')
    print('\t python ' + sys.argv[0] + ' /path/to/csvfile > converted.csv')
else:
    inputfile = sys.argv[1]
    reader = csv.reader(open(inputfile, 'rt'))
    for row in reader:
        dataset = [row[3], row[2], row[1], row[0], row[4], row[5], row[6], row[7], row[8], row[9], '0', row[10]]
        print (','.join(dataset))


# output csv-structure
#MemberID, firstname, middlename, lastname, birthdate, address, city, zipcode, organisation, haspaid, debt, akk
