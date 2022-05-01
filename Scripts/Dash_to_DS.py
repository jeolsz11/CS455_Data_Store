#!/usr/local/bin/python
# Python script to automatize interactions between Dashboard and Data Store
# This program uses the TCP server/client model where:
# Data Store acts as the server due to being hosted on the CS server
# Dash acts as the client due to being external to the CS server

# using websockets to communicate with dash due to dash being browser based

# Module Imports
import sys
import MySQLdb
import json
import asyncio
import websockets

# function to retrive endpoint, then send query result
async def get_metrics(websocket):
    count = 0
    endpoint = await websocket.recv()
    print(f">> Received: {endpoint}")
 
    # Connect to MariaDB Platform
    try: 
       connect = MySQLdb.connect(
	    host="localhost",
	    user="monstore",
	    password="455-mon-store",
	    database="monstore",
	    autocommit=True)
    except MySQLdb.Error as e:
	    print(f">> Error connecting to database: {e}")
	    sys.exit(1)
    else:
	    print(">> Connected to database")

    # Instantiate Cursor
    cursor = connect.cursor()

    # get data from database; currently there is only one query type
    query = "SELECT * FROM devices"
    cursor.execute(query)
    select = cursor.fetchall()
    
    result = "["
    for row in select:
        result += "".join(row)
        result += ","
    result += "".join("]")
    result = result.replace("}},]", "}}]")
	
    await websocket.send(result)
    print(f">> Sent: result\n")


# asyncio event loop
async def main():
    async with websockets.serve(get_metrics, 'cs.csis.work', 8082):
        await asyncio.Future() # run forever


# run acutal program
asyncio.run(main())
