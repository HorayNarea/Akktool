import csv
import sys
import sqlite3


if len(sys.argv) < 2:
    print('Usage:')
    print('\t python ' + sys.argv[0] + ' /path/to/csvfile')
else:
    linecounter = 0
    ignoredcounter = 0
    connection = sqlite3.connect('db.sqlite3')
    connection.text_factory = str
    db = connection.cursor()
    inputfile = sys.argv[1]
    reader = csv.reader(open(inputfile, 'rt'))
    for row in reader:
        try:
            db.execute('INSERT INTO akkreditierung_member VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
            linecounter += 1
        except sqlite3.IntegrityError:
            ignoredcounter += 1
    connection.commit()
    print('Imported ' + str(linecounter) + ' datasets!')
    print('Ignored ' + str(ignoredcounter) + ' datasets...')


# csv-structure
#MemberID,firstname,middlename,lastname,birthdate,address,city,zipcode,organisation,haspaid,debt,akk
