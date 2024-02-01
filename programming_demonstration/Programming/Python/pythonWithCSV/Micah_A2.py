"""
o Assignment #: 2
o Course: PROG23199
o Your full name: MICAH JOSHUA RAHARDJO
o Your Sheridan student #: 991687206
o Instructor's name: Syed Tanbeer
"""
import mysql.connector
import csv

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def create_connection():
    global conn 
    username = "dbadmin"
    pwd = "root"
    try:
        conn = mysql.connector.connect(host="localhost", user=username, password=pwd, database="MyStore") # create conn object using the mysql host name, user name and mysql password
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
    sql = 'Create database if not exists MyStore' # sql command to create a database named 'MyStore'
    try:
        cursor.execute(sql) # excecuting 
    except Exception as err:
        pass
    else:
        print('Database created or exists .........')
        usedb = 'Use MyStore' # sql command to get into a database
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

def insert_records_items(value):
    try:
        sql = "INSERT INTO Items_Micah (iid, name, category, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, value)
        conn.commit()
    except Exception as err:
        pass

def insert_records_transaction(value):
    try:
        sql = "INSERT INTO Transactions (tid, iid, quantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, value)
        conn.commit()
    except Exception as err:
        pass

def insert_records(table_name, value):
    try:
        field_name = "iid int(2), item char(15), amount float(5,2)"
        sql = f"INSERT INTO {table_name} (iid, item, amount) VALUES (%s, %s, %s)"
        cursor.execute(sql,value)
        conn.commit()
    except Exception:
        pass

def delete_data_table(value):
    sql = f'delete from {value}' # clears all rows from the table
    cursor.execute(sql)
    conn.commit()

def read_data(table_name):
    sql = f'Select * from {table_name}'
    cursor.execute(sql) # exectue the command
    result = cursor.fetchall() # store the returned info into a variable
    return result

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Opening the csv file and making it to tuples
with open ("Items_Micah.csv", "r", newline='') as file:
    reader = csv.reader(file)
    next(file)
    data_Items = []
    for line in reader:
        data_Items.append((line[0], line[1], line[2], line[3]))

# Opening txt file and making it into tuples
with open ("Transactions.txt", "r") as file:
    next(file)
    next(file) #skipping 2 lines
    read = file.readlines()
    result = []
    tuples = []
    for x in read:
        result.append(x.rstrip("\n"))
    for x in result:
        string = x.split(" ")
        tuples.append((int(string[0]), int(string[1]), int(string[2])))    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#requirement 5
def req_5(table_dairy, table_fruit, table_meat, table_snacks, table_vegetable):
    data_t = read_data("Transactions")
    data_i = read_data("Items_Micah")
    dict_items = {} #make a dictionary for price refference with key = iid, value = [price, name]
    dairy = [] #every category
    fruit = []
    meat = []
    snacks = []
    vegetable = []

    for d in data_i: #adding to price refference dictionary
        key = d[0]
        value = d[3]
        name = d[1]
        dict_items[key] = [value, name]

    for d in data_t: #appending each item to category list
        itemID = d[1]
        quantity = d[2]
        val = dict_items.get(itemID)
        price = val[0]
        name = val[1]
        amount = quantity*price
        if itemID == 1 :
                fruit.append((itemID, name, amount))
        elif itemID == 2 :
                fruit.append((itemID, name, amount))
        elif itemID == 3 :
                meat.append((itemID, name, amount))
        elif itemID == 4 :
                dairy.append((itemID, name, amount))
        elif itemID == 5 :
                vegetable.append((itemID, name, amount))
        elif itemID == 6 :
                vegetable.append((itemID, name, amount))
        elif itemID == 7 :
                meat.append((itemID, name, amount))
        elif itemID == 8 :
                snacks.append((itemID, name, amount))
        elif itemID == 9 :
                snacks.append((itemID, name, amount))
        else :
                dairy.append((itemID, name, amount))
    
    # So that the values doesn't duplicate
    delete_data_table("categorytotal_dairy")
    delete_data_table("categorytotal_fruit")
    delete_data_table("categorytotal_meat")
    delete_data_table("categorytotal_vegetables")
    delete_data_table("categorytotal_snacks")

    #inserting data
    for d in dairy:
         insert_records(table_dairy, d)
    for f in fruit:
         insert_records(table_fruit, f)
    for m in meat:
         insert_records(table_meat, m)
    for v in vegetable:
         insert_records(table_vegetable, v)
    for s in snacks:
         insert_records(table_snacks, s)        
         
#requirement 8
def req_8():
     data_t = read_data("Transactions")
     data_i = read_data("Items_Micah")
     dict_item = {}
     

     for d in data_i:
        key = d[0]
        value = d[3]
        name = d[1]
        dict_item[key] = [value, name]

     for d in data_t:
        itemID = d[1]
        quantity = d[2]
        val = dict_item.get(itemID)
        price = val[0]
        name = val[1]
        amount = quantity*price
        if quantity >= 3:
             print(f"iid = {itemID}\tname = {name}\tquantity = {quantity}\ttotal price = {amount}")

if __name__ == '__main__':
    #initializing
    #requirement 1 & 2
    create_connection()
    create_cursor()
    create_database()

    # making table for Items_Micah
    name_Items = "Items_Micah"
    meta_Items = "iid INT(2) PRIMARY KEY, name VARCHAR(10), category VARCHAR(15), price FLOAT(5,2)"
    create_table(name_Items, meta_Items)

    #making table for Transactions
    name_Items = "Transactions"
    meta_Items = "tid INT(2) PRIMARY KEY, iid int(2), quantity int(2)"
    create_table(name_Items, meta_Items)

    #making table for Category total
    #reuirement 4
    name_dairy = "CategoryTotal_Dairy"
    name_fruit = "CategoryTotal_Fruit"
    name_meat = "CategoryTotal_Meat"
    name_snacks = "CategoryTotal_Snacks"
    name_vegetable = "CategoryTotal_Vegetables"

    meta_totals = "iid int(2), item char(15), amount float(5,2)"

    create_table(name_dairy, meta_totals)
    create_table(name_fruit, meta_totals)
    create_table(name_meat, meta_totals)
    create_table(name_snacks, meta_totals)
    create_table(name_vegetable,meta_totals)

    #inserting content of Items_Micah
    #requirement 3
    for tuple in data_Items:
        insert_records_items(tuple)

    #inserting content of Transaction
    for tuple in tuples:
        insert_records_transaction(tuple)

    # requirement 5
    req_5(name_dairy, name_fruit, name_meat, name_vegetable, name_snacks)

    #requirement 6
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%req 6%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    choice = input("Please enter a category (dairy, fruit, meat, vegetables, snacks): ")
    print("")
    # calculating for all category
    dairy = read_data(name_dairy)
    total_dairy = 0
    for x in dairy:
        total_dairy += x[2]

    fruit = read_data(name_fruit)
    total_fruit = 0
    for x in fruit:
        total_fruit += x[2]

    meat = read_data(name_meat)
    total_meat = 0
    for x in meat:
        total_meat += x[2]

    snacks = read_data(name_snacks)
    total_snacks = 0
    for x in snacks:
        total_snacks += x[2]

    vegetable = read_data(name_vegetable)
    total_vegetable = 0
    for x in vegetable:
        total_vegetable += x[2]
       
    #printing the chosen category
    
    if choice == "dairy" :
        dairy = read_data(name_dairy)
        for x in dairy:
            print (f"id = {x[0]}\tname = {x[1]}\tprice = {x[2]}")
        print (f"the totals are {total_dairy}")

    if choice == "fruit" :
        fruit = read_data(name_fruit)
        for x in fruit:
            print (f"id = {x[0]}\tname = {x[1]}\tprice = {x[2]}")
        print (f"the totals are {total_fruit}")

    if choice == "meat" :
        meat = read_data(name_meat)
        for x in meat:
            print (f"id = {x[0]}\tname = {x[1]}\tprice = {x[2]}")
        print (f"the totals are {total_meat}")

    if choice == "snacks" :
        snacks = read_data(name_snacks)
        for x in snacks:
            print (f"id = {x[0]}\tname = {x[1]}\tprice = {x[2]}")
        print (f"the totals are {total_snacks}")

    if choice == "vegetables" :
        vegetable = read_data(name_vegetable)
        for x in vegetable:
            print (f"id = {x[0]}\tname = {x[1]}\tprice = {x[2]}")
        print (f"the totals are {total_vegetable}")

    # requirement 7
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%req 7%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    total_amount = total_meat + total_dairy + total_fruit + total_snacks + total_vegetable
    print ("")
    print(f"Total amount of all transactions {total_amount}")
    print("")

    #requirement 8
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%req 8%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    req_8()

    #requirement 9
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%req 9%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    ipt = input("\nPlease enter a coloumn name: ")
    sql = f"select {ipt} from Items_Micah"
    cursor.execute(sql)
    for lines in cursor:
        print(lines) 


