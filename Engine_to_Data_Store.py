#!/usr/bin/python
# PYTHON SCRIPT TO AUTOMIZE DATABASE

# Module Imports
import MySQLdb
import sys
import json

# Connect to MariaDB Platform
try:
	conn = MySQLdb.connect(
	host="cs.csis.work",
	port=22,
	user="monstore",
	password="455-mon-store",
	autocommit=True
)
except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)

# Instantiate Cursor
cursor = conn.cursor()

# hard coded JSON for testing in isolation
json_data = '{ "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }'

# add data
cursor.execute("INSERT INTO devices() VALUES('" + json_data + "')")

# update data
cursor.execute('''
	SELECT 
	JSON_REPLACE(metrics, '$.Time Stamp', 'new_time'), 
	JSON_REPLACE(metrics, '$.CPU', 'new_cpu'),
	JSON_REPLACE(metrics, '$.DISK', 'new_disk'),
	JSON_REPLACE(metrics, '$.MEMORY', 'new_memory'),
	JSON_REPLACE(metrics, '$.NETWORK', 'new_network'),
	FROM devices WHERE JSON_VALUE(metrics, '$.ID') = '4486d8dc-9258-45e1-8a41-816bcd6f5ea3'
''')
conn.commit()

# close connection
conn.close()
