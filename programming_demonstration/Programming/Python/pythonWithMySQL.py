"""
Micah
991687206
"""
import mysql.connector
import csv

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def create_connection():
    global conn 
    username = "root"
    pwd = "root"
    try:
        conn = mysql.connector.connect(host="localhost", user=username, password=pwd, database="TourDB_Micah") # create conn object using the mysql host name, user name and mysql password
    except Exception as err:
        print(err)
    else:
        print(conn)
        print('Connection to the database established...')

def create_cursor():
    global cursor # use a cursor to execute any command on mysql from Python 
    cursor = conn.cursor() # create a cursor using for the conn object
    print('Cursor created ............')

def create_database():
    sql = 'Create database if not exists TourDB_Micah' # sql command to create a database named 'MyStore'
    try:
        cursor.execute(sql) # excecuting 
    except Exception as err:
        pass
    else:
        print('Database created or exists .........')
        usedb = 'Use tourDB_Micah' # sql command to get into a database
        cursor.execute(usedb) # execute
        print ('Database changed......')

def create_table(table_name, meta_Data):
    try:
        sql = f'CREATE TABLE {table_name} ({meta_Data})' # sql command to create a table
        cursor.execute(sql) 
    except Exception as err:
        pass
    else:
        print('Table created or exists ...')

def insert_into_table(table, data, value):
    cursor.execute(f'INSERT INTO tourDB_Micah.{table} ({data}) VALUES ({value})')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

create_connection()
create_cursor()
create_database()
create_table('Packages', 'id INT PRIMARY KEY, name VARCHAR(50), unitPrice FLOAT, rating FLOAT')
create_table('Purchases', 'pid INT, pkgID INT, quantity INT')

package_data = 'id, name, unitPrice, rating'

package_value = {
    1 : [1, 'Toronto', 200, 4.5],
    2 : [2, "Montreal", 320, 4.0],
    3 : [3, "London", 250, 4.2],
    4 : [4, "Paris", 450, 3.4]
                 }

for k,v in package_value.items():
    value = f'{v[0]},{v[1]},{v[2]},{v[3]}'
    print (value)
    insert_into_table('Packages', package_data, value)


Purchases_data = 'pid, pkgID, quantity'
Purchases_value = {
    1 : [1, 3, 3],
    2 : [2, 1, 2],
    3 : [3, 2, 1],
    4 : [4, 1, 2],
    5 : [5, 2, 1]
                 }

"""for k,v in Purchases_value.items():
    value = f'{v[0]},{v[1]},{v[2]}'
    insert_into_table('Purchases', Purchases_data, value)"""

cursor.execute('Describe Packages')
cursor.execute('Describe Purchases')
cursor.execute('select * from Packages')
cursor.execute('select * from Purchases')

for n in cursor:
    print (n)

