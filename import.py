import csv
import sys
import sqlite3


if len(sys.argv) < 2:
    print 'Usage:'
    print '\t python ' + sys.argv[0] + ' /path/to/csvfile'
else:
    connection = sqlite3.connect('db.sqlite3')
    connection.text_factory = str
    db = connection.cursor()
    inputfile = sys.argv[1]
    with open(inputfile, 'rb') as f:
        reader = csv.reader(f)
        linecounter = 0
        for row in reader:
            db.execute('INSERT INTO akkreditierung_member VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
            linecounter += 1
        connection.commit()
        print 'Imported ' + str(linecounter) + ' datasets!'

# csv-structure
#MemberID,firstname,middlename,lastname,birthdate,address,city,zipcode,organisation,haspaid,debt,akk
