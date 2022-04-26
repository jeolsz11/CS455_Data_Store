#!/usr/local/bin/python
# Python script to automatize interactions between Dashboard and Data Store
# This program uses the TCP server/client model where:
# Data Store acts as the server due to being hosted on the CS server
# Dash acts as the client due to being external to the CS server

# Module Imports
import sys
import MySQLdb
import json
import socket

# specify Host and Port 
HOST = 'localhost' 
PORT = 8082

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding host and port
try:
    s.bind((HOST, PORT))    
except socket.error as message:
    print('>> Bind failed.')
    sys.exit() 
else: 
    print('>> Socket binded')
   
# starts listening
s.listen()
print ('>> Listening...')
   
# receive from Dash   
#while True:
connect, addr = s.accept() # establish connection with Dash
print ('>> Connected')
query = connect.recv(1024).decode('utf-8')
print ('>> Received ', repr(query))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Connect to MariaDB Platform
#try: 
#   connect = MySQLdb.connect(
#	host="localhost",
#	user="monstore",
#	password="455-mon-store",
#	database="monstore",
#	autocommit=True)
#except MySQLdb.Error as e:
#	print(f"Error connecting to database: {e}")
#	sys.exit(1)
#else:
#	print("Connected to database")

# Instantiate Cursor
#cursor = connect.cursor()

# get data from database; currently there is only one query type
#query = "SELECT * FROM devices"
#cursor.execute(query)

# write results to metrics.json; writing over what was previously there
#json_object = json.dumps(dictionary, indent = 4)
#with open("metrics.json", "w") as outfile:
#outfile.write(json_object)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

filename = 'metrics.json' # file MUST be in same folder or path as program
file = open(filename,'rb')
l = file.read(1024)

#while (l):
connect.sendall('Data Store'.encode('utf-8'))
print('>> Sent ', repr(l))
l = file.read(1024)
file.close()

print('>> Done sending')

# close socket and connection		
s.close()
connect.close()
