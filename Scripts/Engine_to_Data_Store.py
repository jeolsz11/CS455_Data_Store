#!/usr/local/bin/python

# PYTHON SCRIPT TO AUTOMIZE DATABASE

# Module Imports
import MySQLdb
import sys
import json
import socket

def insert_into_database(db, json_data):
    # Instantiate Cursor
    cursor = db.cursor()

    # Testing SELECT so show everything in the devices table
    cursor.execute('SELECT * FROM devices')
    for i in cursor:
        data = cursor.fetchone()
        if data:
            #print(i)
            #print()
            print(data)
            print()
        else:
            print("Error") 

    query = 'INSERT INTO devices() VALUES(%s)'
    try:
	    cursor.execute(query, (json.dumps(json_data),))
    except:
        print("Failed to insert values")
    else:
        db.commit()
        # Print that 1 row was inserted if successful  
        print(cursor.rowcount, "record inserted.") 
        print()

    # Print table with the new row that was inserted 
    cursor.execute('SELECT * FROM devices')
    for i in cursor:
        data = cursor.fetchone()
        if data:
            #print(i)
            #print()
            print(data)
            print()
        else:
            print("Error")


HOST = "localhost"
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        soc.bind((HOST, PORT))
    except:
        print("Bind failed.")
        sys.exit()
    else:
        print("Socket Binded.") 
        soc.listen()
        print("Listening...")
        conn, addr = soc.accept()
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        with conn:
            print(f"Connected by {addr}")
            while True:
                json_data = conn.recv(1024).decode()
                print("Received: ", json_data) 
                if not json_data:
                    break                
                try:
                    db = MySQLdb.connect("localhost","monstore","455-mon-store","monstore")
                except:
                    print("Can't connect to database")
                else:
                    #successful connection
                    print("Connected to database")
                    print()
                    insert_into_database(db, json_data)
		            # Close connection
                    db.close()
                #conn.sendall(json_data)
                #conn.sendall.encode("UTF-8") 


# Try to connect to the database
"""
try:
    db = MySQLdb.connect("localhost","monstore","455-mon-store","monstore")
except:
    print("Can't connect to database")
else:
    #successful connection
    print("Connected to database")
    print()
"""
"""
# Instantiate Cursor
cursor = db.cursor()
	
# Hard coded JSON for testing in isolation
#json_data = '{ "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }'

# Testing SELECT so show everything in the devices table
cursor.execute('SELECT * FROM devices')
for i in cursor:
    data = cursor.fetchone()
    if data:
        #print(i)
        #print()
        print(data)
        print()
    else:
        print("Error") 

# Add data
# Try to insert new values into the devices table
json_data1 = { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }
json_data2 = { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea1", "Time Stamp": "22:01:29", "CPU": 1, "DISK": 40, "MEMORY": 30, "NETWORK": 2 }
json_data3 = { "ID": "00ce9834-8453-4580-8082-4d2748c84e65", "Time Stamp": 1650469613, "CPU": 10, "DISK": 3, "MEMORY": 66, "NETWORK": { "BYTES SENT": 1554241536, "BYTES RECIEVED": 3376441344 } }
query = 'INSERT INTO devices() VALUES(%s)'

try:
	cursor.execute(query, (json.dumps(json_data),))
except:
    print("Failed to insert values")
else:
    db.commit()
    # Print that 1 row was inserted if successful  
    print(cursor.rowcount, "record inserted.") 
    print()

# Print table with the new row that was inserted 
cursor.execute('SELECT * FROM devices')
for i in cursor:
    data = cursor.fetchone()
    if data:
        #print(i)
        #print()
        print(data)
        print()
    else:
        print("Error") 
"""

# Close sockets
#conn.close()
#soc.close()
# Close connection
#db.close()

