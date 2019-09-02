import json
import mysql.connector
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

