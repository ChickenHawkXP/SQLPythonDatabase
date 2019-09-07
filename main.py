import json
import mysql.connector

table = "PYTABLE"
row_list = dict()
def menu():
    print('\nWhat would you like to do?:\n [1] Add user to the database\n [2] Remove user from database\n [3] Output database\n [4] Search by column\n [5] Edit Column\n [6] Exit')

def param_menu():
    print("\nWhat parameters would you like to search by?\n [1] Name\n [2] Age\n [3] Date of Birth\n [4] Height\n [5] Number of pets\n [6] Back\n")

def printCols():
    print("\n[1] Name\n[2] Age\n[3] Date of Birth\n[4] Height\n[5] # of Pets\n")
#Prints the contents of the database to the console
def printTable(db):
    row_list.clear()
    index = 0
    for i in db:
        index += 1
        row_list.update({index:i})
    print('\n%d record(s) found!\n' %index)
    if index == 0:
        return index
    count = 1
    for x in row_list:
        print(count,'.',row_list.get(x))
        count += 1
    
#Displays the contents of the database
def displayDB(db):
    db.execute("SELECT * FROM %s" %table)
    printTable(db)
    records = printTable(db)
    return records

#A function to add rows into the database
def add_data(db,connector):
    name = input("Enter your first and last name: ")
    age = int(input("Enter your age: "))
    dob = input("Enter your date of birth (mmm-dd-yyyy): ")
    height = input("Enter your height (in inches.): ")
    pets = int(input("Enter the amount of pets you have: "))
    db.execute("""INSERT INTO `%s`
                  VALUES ('%s',%d,'%s','%s',%d);""" %(table,name,age,dob,height,pets))
    connector.commit()

#A function that displays text for filter
def search_by(db,connector):
    param_menu()
    choice = input()
    if choice == '1':
        print("Enter the name you are looking for: ")
        name = input()
        db.execute("""SELECT *
                      FROM %s
                      WHERE `NAME` LIKE '%%%s%%'""" %(table, name))
        try:
            printTable(db)
        except TypeError:
            print("\nNo results could be found!\n")
    if choice == '2':
        print('Enter the age of the person:')
        age = int(input())
        db.execute("""SELECT *
                      FROM %s
                      WHERE `AGE` = %d""" %(table, age))
        try:
            printTable(db)
        except TypeError:
            print("\nNo results could be found!\n")
    if choice == '3':
        print('Enter the persons birthday(mmm-dd-yyyy):')
        dob = input()
        db.execute("""SELECT *
                      FROM %s
                      WHERE `DOB` LIKE '%s%%'""" %(table, dob))
        try:
            printTable(db)
        except TypeError:
            print("\nNo results could be found!\n")
    if choice == '4':
        print('Enter the persons height (in inches):')
        height = int(input())
        db.execute("""SELECT *
                      FROM %s
                      WHERE `HEIGHT` = %d""" %(table, height))
        try:
            printTable(db)
        except TypeError:
            print("\nNo results could be found!\n")
    if choice == '5':
        print('Enter the amount of pets this person has:')
        pets = int(input())
        db.execute("""SELECT *
                      FROM %s
                      WHERE `PETS` = %d""" %(table, pets))
        try:
            printTable(db)
        except TypeError:
            print("\nNo results could be found!\n")

#A function that allows you change column data
def changeCol(db,connector):
    records = printTable(db)
    try:
        if records < 1:
            print("There are no records to change!\n")
            return
    except TypeError:
        pass
    choice = int(input("\nSelect an entry to change: "))
    if choice in row_list:
        data = row_list.get(choice)
    printCols()
    change = input("\nWhich column would you like to chage?: ")
    if change == '1':
        name = input("\nWhat would you like to change the name to?: ")
        db.execute("""UPDATE %s
                      SET `NAME` = '%s'
                      WHERE `NAME` = '%s'
                      AND `AGE` = %d
                      AND `DOB` = '%s'
                      AND `HEIGHT(in.)` = '%s'
                      AND `PETS` = %d""" %(table,name,data[0],data[1],data[2],data[3],data[4]))
        connector.commit()
    if change == '2':
        name = input("\nWhat would you like to age to?: ")
        db.execute("""UPDATE %s
                      SET `AGE` = '%s'
                      WHERE `NAME` = '%s'
                      AND `AGE` = %d
                      AND `DOB` = '%s'
                      AND `HEIGHT(in.)` = '%s'
                      AND `PETS` = %d""" %(table,name,data[0],data[1],data[2],data[3],data[4]))
        connector.commit()
    if change == '3':
        name = input("\nWhat would you like to change the date of birth to?(mmm-dd-yyyy): ")
        db.execute("""UPDATE %s
                      SET `DOB` = '%s'
                      WHERE `NAME` = '%s'
                      AND `AGE` = %d
                      AND `DOB` = '%s'
                      AND `HEIGHT(in.)` = '%s'
                      AND `PETS` = %d""" %(table,name,data[0],data[1],data[2],data[3],data[4]))
        connector.commit()
 
    if change == '4':
        name = input("\nWhat would you like to change the height to: ")
        db.execute("""UPDATE %s
                      SET `HEIGHT(in.)` = '%s'
                      WHERE `NAME` = '%s'
                      AND `AGE` = %d
                      AND `DOB` = '%s'
                      AND `HEIGHT(in.)` = '%s'
                      AND `PETS` = %d""" %(table,name,data[0],data[1],data[2],data[3],data[4]))
        connector.commit()
    if change == '5':
        name = input("\nWhat would you like to change the # of pets to: ")
        db.execute("""UPDATE %s
                      SET `PETS` = '%s'
                      WHERE `NAME` = '%s'
                      AND `AGE` = %d
                      AND `DOB` = '%s'
                      AND `HEIGHT(in.)` = '%s'
                      AND `PETS` = %d""" %(table,name,data[0],data[1],data[2],data[3],data[4]))
        connector.commit()

#Deletes a selected column
def deleteCol(db,connector):
    records = printTable(db)
    try:
        if records < 1:
            print("There are no records to delete!\n")
            return
    except TypeError:
        pass
    choice = int(input("Select an entry to delete: "))
    if choice in row_list:
        data = row_list.get(choice)
    delete = input("\nAre you sure you want to delete this case? (yes/no): ")
    if(delete == "yes"):
        db.execute("""DELETE FROM %s
                      WHERE `NAME` = '%s'
                      AND `AGE` = %d
                      AND `DOB` = '%s'
                      AND `HEIGHT(in.)` = '%s'
                      AND `PETS` = %d""" %(table,data[0],data[1],data[2],data[3],data[4]))
        connector.commit()
    else:
        return

#Open the JSON with the SQL information
with open("config.json") as json_read:
    data = json.load(json_read)
try:
    database = mysql.connector.connect(host = data['host'],
                                       user = data['user'],
                                       password = data['password'],
                                       database = data['database'],
                                       auth_plugin = data['auth_plugin'])
except:
    print('Could not make connection with database!')
cursor = database.cursor(buffered = True)
choice = '0'
while choice != '6':
    menu()
    choice = input()
    if choice == '1':
        add_data(cursor,database)
    if choice == '2':
        cursor.execute("SELECT * FROM %s" %table)
        deleteCol(cursor,database)
    if choice == '3':
        cursor.execute("SELECT * FROM %s" %table)
        printTable(cursor)
    if choice == '4':
        cursor.execute("SELECT * FROM %s" %table)
        search_by(cursor,database)
    if choice == '5':
        cursor.execute("SELECT * FROM %s" %table)
        changeCol(cursor,database)
cursor.close()
database.close()
    
