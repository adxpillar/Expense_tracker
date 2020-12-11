import os, sqlite3, sys

# check to see if proper file path+name is entered 
try:
    sys.argv[1]
except IndexError:
    print("Error - missing input file name! Usage ./copy.py input txt file")
else:
    expenseFile = sys.argv[1]

# check whether file exists and is accessible 

if not os.path.isfile(expenseFile):
    print("Error - input file, expenseFile, is not accessible!")
    sys.exit(1)
else:
    f = open(expenseFile, 'r')

conn = sqlite3.connect('./db.sqlite3')
cursor = conn.cursor()

sql = ''' CREATE TABLE Expense (
    Title CHAR(20) NOT NULL,
    Amount FLOAT NOT NULL,
    Created_at CHAR(20) NOT NULL,
    Tags TEXT 
) '''

# dummy proof drop and create to create table regardless
try:
    cursor.execute(''' DROP TABLE IF EXISTS Expense''')
except IndexError:
    print("Table not dropped or no such tables")
finally:
    cursor.execute(sql)


count = 0
for line in f.readlines():
    line = [l.strip() for l in line.split(',')]
    title = line[0]
    amount = line[1]
    created_at = line[2]
    tags = line[3].replace(' ',',')


    try:
        cursor.execute('Insert INTO Expense (Title,Amount,Created_at,Tags) VALUES (?,?,?,?)', (title,amount,created_at,tags))
    except:
        print("Unable to write records")
    count += 1
conn.commit()
print(count, 'records were processed')
f.close()


