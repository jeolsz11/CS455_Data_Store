#!/usr/local/bin/python
# PYTHON SCRIPT FOR DASH TO INTERACT WITH DATABASE 
# Module Imports
import MySQLdb
import json
import socket
import sys
  
# specify Host and Port 
HOST = 'localhost' 
PORT = 

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding host and port
try:
    soc.bind((HOST, PORT))    
except socket.error as message:
    print('Bind failed.')
    sys.exit()  
print('Socket binded')
   
# starts listening
soc.listen(9)
   
conn, address = soc.accept()
# print the address of connection
print('Connected with ' + address[0] + ':' + str(address[1]))

# Connect to MariaDB Platform
try: 
connect = MySQLdb.connect(
	host="localhost",
	user="monstore",
	password="455-mon-store",
	database="monstore",
	autocommit=True)
except MySQLdb.Error as e:
	print(f"Error connecting to database: {e}")
	sys.exit(1)
print("Connected to database")

# Instantiate Cursor
cursor = connect.cursor()

# receive endpoint from Dash to get query (e.g. 127.0.0.1/serverstatus)
endpoint = 

# get data from database; currently there is only one query type
query = "SELECT * FROM devices"
cursor.execute(query)

# compile resutls into JSON format text file

# Data to be written
result ={"ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8}

# Serializing json 
json_object = json.dumps(dictionary, indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# send dash text file


# close connection
connect.close()
