import json
import mysql.connector
table = "PYTABLE"
def menu():
    print('What would you like to do?:\n [1] Add user to the database\n [2] Remove user from database\n [3] Output database\n [4] Search by column [5] Exit')
def displayDB(db):
    db.execute("SELECT * FROM %s" %table)
    try:
        for i in db:
            print(i)
    except TypeError:
        print("The database is empty! Please add some information")

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
while choice != '4':
    menu()
    choice = input()
    if choice == '1':
        add_data(cursor,database)
    if choice == '2':
        break
    if choice == '3':
        displayDB(cursor)
    if choice == '4':
        break
cursor.close()
database.close()
    
