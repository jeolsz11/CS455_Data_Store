#!/usr/local/bin/python

# PYTHON SCRIPT TO AUTOMIZE DATABASE.
# This script automizes interactions between the Engine and the Data Store.
# This program receives JSON data from the Engine and then inserts the data into the Data Store which is a MariaDB database.
# The Data Store acts as a server due to being hosted on the CS server.

# Module Imports.
import MySQLdb
import sys
import json
import socket

# Function to insert data into the database.
def insert_into_database(db, json_data):
    # Instantiate Cursor.
    cursor = db.cursor()

    # SQL query to insert into the error_log table in the database.
    query4 = 'INSERT INTO error_log(error) VALUES(%s)'
    
    
    # If an error message is sent, insert it into the error_log table in the database.
    if(json_data[0] != "{"):
        try:
            cursor.execute(query4, (json.dumps(json_data),))
        except:
            print("Failed to insert error message")
        else:
            db.commit()
            print(cursor.rowcount, "record inserted into error_log table.")
            print()
            cursor.execute('SELECT * FROM error_log')
            for i in cursor:
                data = cursor.fetchone()
                if data:
                    print(data)
                    print()
		    return	
                else:
                    print("Error printing data")
                    return

    # Testing SELECT so show everything that is currently in the devices table.
    cursor.execute('SELECT * FROM devices')
    for i in cursor:
        data = cursor.fetchone()
        if data:
            print(data)
            print()
        else:
            print("Error printing data") 
   
    # Adding double quotes where they need to be so that the received data is in proper JSON format.
    char1 = "ID: "
    json_data = json_data.replace(char1, "\"ID\": \"")

    char1 = ", Time Stamp: "
    json_data = json_data.replace(char1, "\", \"Time Stamp\": ")

    char1 = "CPU: "
    json_data = json_data.replace(char1, "\"CPU\": ")

    char1 = "DISK: "
    json_data = json_data.replace(char1, "\"DISK\": ")

    char1 = "MEMORY: "
    json_data = json_data.replace(char1, "\"MEMORY\": ")

    char1 = "NETWORK: "
    json_data = json_data.replace(char1, "\"NETWORK\": ")

    char1 = "BYTES SENT: "
    json_data = json_data.replace(char1, "\"BYTES SENT\": ")

    char1 = "BYTES RECEIVED: "
    json_data = json_data.replace(char1, "\"BYTES RECEIVED\": ")

    #print(json_data)
    #print() 

    # Convert from a string to JSON.
    json1 = json.loads(json_data)
    
    # Get the ID number of the received data to check if this particular device is already in the database.
    json_id = json1["ID"]
    json_id1 = (str(json_id), )
    
    # SQL queries to insert into and delete from the devices table in the database.
    query = 'INSERT INTO devices() VALUES(%s)'
    #query2 = 'SELECT JSON_VALUE(metrics, "$.ID") AS id FROM devices' 
    query3 = 'DELETE FROM devices WHERE JSON_VALUE(metrics, "$.ID") = %s'

    # Try and see if the particular device ID that was received from the Engine is already in the database.
    # If it is already in the database, delete it from the database. 
    # The new data that was received will be inserted into the database instead.
    try:
        cursor.execute(query3, json_id1)
    except:
        print("No duplicates were deleted")
    else:
        db.commit()
        # Print how many rows were deleted.
        print(cursor.rowcount, "record(s) deleted from devices table.")

    # Try to insert data into the database.
    try:
	    cursor.execute(query, (json.dumps(json1),))
    except:
        print("Failed to insert values")
    else:
        db.commit()
        # Print that 1 row was inserted if successful.  
        print(cursor.rowcount, "record inserted into devices table.") 
        print()

    # Print the devices table with the new row that was inserted. 
    cursor.execute('SELECT * FROM devices')
    for i in cursor:
        data = cursor.fetchone()
        if data:
            print(data)
            print()
        else:
            print("Error printing data")


# Host and Port to listen on.
HOST = "localhost"
PORT = 8081

# Using sockets to listen for incoming messages from the Engine.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Try to bind the socket.
    try:
        soc.bind((HOST, PORT))
    except:
        print("Bind failed.")
        sys.exit()
    else:
        # Successful binding.
        print("Socket Binded.") 
        # Listen for the Engine.
        soc.listen()
        print("Listening...")
        conn, addr = soc.accept()
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        with conn:
            print(f"Connected by {addr}")
            while True:
                json_data = conn.recv(1024).decode()
                # Print what was received from the Engine.
                print("Received: ", json_data) 
                if not json_data:
                    break                
                # Try to connect to the database.
                try:
                    db = MySQLdb.connect("localhost","monstore","455-mon-store","monstore")
                except:
                    print("Can't connect to database")
                else:
                    # Successful connection.
                    print("Connected to database")
                    print()
                    # Insert data into the database.
                    insert_into_database(db, json_data)
		    # Close connection
                    db.close()


