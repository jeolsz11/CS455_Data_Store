# PYTHON SCRIPT FOR DASH TO INTERACT WITH DATABASE 
	# Module Imports
	import mariadb
	import sys
	
	
	// receive endpoint from Dash to get quer (e.g. 127.0.0.1/serverstatus)
	// get data from database
	// compile resutls into JSON format text file
	// send dash text file
	
	
	# Connect to MariaDB Platform
	try:
		conn = mariadb.connect(
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
	json_data = "{ "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }"
	
	# select data
	cursor.execute(
		"SELECT * FROM JSON_TABLE()
		JSON_VALUE(metrics, '$.ID') AS device_ID 
		JSON_VALUE(metrics, '$.Time Stamp') AS time_stamp, 
		JSON_VALUE(metrics, '$.CPU') AS cpu_usage,
		JSON_VALUE(metrics, '$.DISK') AS disk_usage,
		JSON_VALUE(metrics, '$.MEMORY') AS memory_usage,
		JSON_VALUE(metrics, '$.NETWORK') AS network_usage 
		FROM devices WHERE JSON_VALUE(metrics, '$.ID') = '4486d8dc-9258-45e1-8a41-816bcd6f5ea3'"
	)
	# Print Result-set
	for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")
	
	# close connection
	conn.close()
