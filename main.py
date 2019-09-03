import json
import mysql.connector

table = "PYTABLE"
def menu():
    print('What would you like to do?:\n [1] Add user to the database\n [2] Remove user from database\n [3] Output database\n [4] Search by column\n [5] Exit')

#Prints the contents of the database to the console
def printTable(db):
    index = 0
    for i in db:
        index += 1
        print(i)
    print('\n%d record(s) found!\n' %index)

#Displays the contents of the database
def displayDB(db):
    db.execute("SELECT * FROM %s" %table)
    try:
        printTable(db)
    except TypeError:
        print("The database is empty! Please add some information")

#A function to add rows into the database
def add_data(db,connector):
    print("Enter your first and last name: ")
    name = input()
    print("Enter your age: ")
    age = int(input())
    print("Enter your date of birth (mmm-dd-yyyy): ")
    dob = input()
    print("Enter your height (in inches.): ")
    height = input()
    print("Enter the amount of pets you have: ")
    pets = int(input())
    db.execute("""INSERT INTO `%s`
                  VALUES ('%s',%d,'%s','%s',%d);""" %(table,name,age,dob,height,pets))
    connector.commit()

#A function that displays text for filter
def search_by(db,connector):
    print("\nWhat parameters would you like to search by?\n [1] Name\n [2] Age\n [3] Date of Birth\n [4] Height\n [5] Number of pets\n [6] Back\n")
    choice = input()
    if choice == '1':
        print("Enter the name you are looking for: ")
        name = input()
        db.execute("""SELECT *
                      FROM %s
                      WHERE `NAME` LIKE '%s%%'""" %(table, name))
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
while choice != '5':
    menu()
    choice = input()
    if choice == '1':
        add_data(cursor,database)
    if choice == '2':
        break
    if choice == '3':
        displayDB(cursor)
    if choice == '4':
        search_by(cursor,database)
cursor.close()
database.close()
    
