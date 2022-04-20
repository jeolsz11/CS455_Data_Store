#!/usr/local/bin/python

# PYTHON SCRIPT TO AUTOMIZE DATABASE

# Module Imports
import MySQLdb
#import sys
import json
import socket

HOST = "localhost"
PORT = # port to listen on 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind((HOST, PORT))
    soc.listen()
    conn, addr = soc.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            json_data = conn.recv(1024)
            if not json_data:
                break
            conn.sendall(json_data) 

# Connect to MariaDB Platform
#try:
#	conn = MySQLdb.connect(
#	host="cs.csis.work",
#	port=22,
#	user="monstore",
#	password="455-mon-store",
#	autocommit=True
#	)
#except MySQLdb.Error as e:
#	print(f"Error connecting to MariaDB Platform: {e}")
#	sys.exit(1)

# try to connect to the database
try:
    db = MySQLdb.connect("localhost","monstore","455-mon-store","monstore")
except:
    print("Can't connect to database")
else:
    #successful connection
    print("Connected to database") 

# Instantiate Cursor
cursor = db.cursor()
	
# hard coded JSON for testing in isolation
#json_data = '{ "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }'

# testing SELECT so show everything in the devices table
cursor.execute('SELECT * FROM devices')
for i in cursor:
    data = cursor.fetchone()
    if data:
        print(data)
    else:
        print("Error") 

# add data
#try:
#	cursor.execute("INSERT INTO devices() VALUES('" + json_data + "')")
#except:
#    print("Failed to insert values") 


# try to insert new values into the devices table
json_data1 = { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }
json_data2 = { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea1", "Time Stamp": "22:01:29", "CPU": 1, "DISK": 40, "MEMORY": 30, "NETWORK": 2 }
query = 'INSERT INTO devices() VALUES(%s)'

try:
	cursor.execute(query, (json.dumps(json_data),))
except:
    print("Failed to insert values")
else:
    db.commit()
    # print that 1 row was inserted if successful  
    print(cursor.rowcount, "record inserted.") 

# print table with the new row that was inserted 
cursor.execute('SELECT * FROM devices')
for i in cursor:
    data = cursor.fetchone()
    if data:
        print(data)
    else:
        print("Error") 

# update data
#	cursor.execute('''
#    SELECT 
#		JSON_REPLACE(metrics, '$.Time Stamp', 'new_time'), 
#		JSON_REPLACE(metrics, '$.CPU', 'new_cpu'),
#		JSON_REPLACE(metrics, '$.DISK', 'new_disk'),
#		JSON_REPLACE(metrics, '$.MEMORY', 'new_memory'),
#		JSON_REPLACE(metrics, '$.NETWORK', 'new_network'),
#		FROM devices WHERE JSON_VALUE(metrics, '$.ID') = '4486d8dc-9258-45e1-8a41-816bcd6f5ea3'
#        ''')

#db.commit()
	
# close connection
db.close()

