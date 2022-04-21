The Data Store will use the MariaBD RDBS on the CS server for storage, and have two Pythin scripts for automatizing connections with the Engine and Dashboard respectively.
  
  
Use ssh (secure shell) to access server (ssh is already built into CS server)
 

To work in the database we will use command line tool mysql
   - To create and test database off server (such as on your personal device) download mariaBD OR XAMMP
   - To access database on CS server, log into server as yourself, then log into database using monstore username and password

----------------------------------------------------------------------------------------------------
Start MySQL in XAMPP Control Panel then open shell to the right
```
username@USERNAME c:\xampp
# mysql -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.4.24-MariaDB mariadb.org binary distribution
```
Now either select database 
```
MariaDB [(none)]> use monstore;
```
or create one	
```
MariaDB [(none)]> CREATE DATABASE monstore; 
MariaDB [(none)]> use monstore;
 ```
	
It should say "Database changed" to show you are in that database

NOTES
	delete database
		MariaDB [(none)]> DELETE DATABASE monstore;
	show exsisitng databases 
		MariaDB [(none)]> show databases;
	to view all tables in database
		MariaDB [monstore]> show tables;


Table creation statements (copy & paste directly into shell)
```
MariaDB [monstore]> CREATE TABLE devices (metrics JSON);
MariaDB [monstore]> CREATE TABLE error_log (error JSON, date varchar(10));
```
View entire tables untabulated	
```
MariaDB [monstore]> SELECT * FROM devices;
MariaDB [monstore]> SELECT * FROM error_log;
```
	
The Engine receives JSON formatted data and performs a sanity check on it
Once data is checked, it is sent to the database to be stored
Data will be continuously sent; menaing entries will need to be continuously updated.
An ID is in the data to keep track of it's association to it's device

```
EXAMPLE JSON DATA SENT BY AGENTS
	{ "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }
```

Assuming tables are already created
```
MariaDB [monstore]> INSERT INTO devices() VALUES('{ "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }');	
MariaDB [monstore]> INSERT INTO error_log() VALUES('{"Message": "meow", "Device": 45}','04.04.2022');
```
	
Show metrics of all devices / AKA show entire table
```
MariaDB [monstore]> SELECT * FROM devices;
+-----------------------------------------------------+
| metrics                                             |
+-----------------------------------------------------+
| { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3",     |
|  "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44,    |
|  "MEMORY": 31, "NETWORK": 8 }                       |
+-----------------------------------------------------+
|                 additonal rows here                 |
+-----------------------------------------------------+

MariaDB [monstore]> SELECT * FROM error_log
+-----------------------------------+------------+
| error                             |    date    |
+-----------------------------------+------------+
| {"Message": "meow", "Device": 45} | 04.04.2022 | 
+------------------------------------------------+
|               additonal rows here              |
+------------------------------------------------+
```

Show metrics of specific device by ID
```
	MariaDB [monstore]> SELECT * FROM devices WHERE JSON_VALUE(metrics, '$.ID') = '4486d8dc-9258-45e1-8a41-816bcd6f5ea3';
	+-----------------------------------------------------+
	| metrics                                             |
	+-----------------------------------------------------+
	| { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3",     |
	|  "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44,    |
	|  "MEMORY": 31, "NETWORK": 8 }                       |
	+-----------------------------------------------------+
 ```

Show specific metric of all devices
```
	MariaDB [monstore]> SELECT JSON_VALUE(metrics, '$.CPU') AS cpu_usage FROM devices;
	+-----------+
	| cpu_usage |
	+-----------+
	| 8         |
	+-----------+
	| etc       |
	+-----------+
  ```

Show tabulated metrics of specific device by ID
```
	MariaDB [monstore]> 
	SELECT 
	JSON_VALUE(metrics, '$.ID') AS device_ID 
	JSON_VALUE(metrics, '$.Time Stamp') AS time_stamp, 
	JSON_VALUE(metrics, '$.CPU') AS cpu_usage,
	JSON_VALUE(metrics, '$.DISK') AS disk_usage,
	JSON_VALUE(metrics, '$.MEMORY') AS memory_usage,
	JSON_VALUE(metrics, '$.NETWORK') AS network_usage 
	FROM devices WHERE JSON_VALUE(metrics, '$.ID') = '4486d8dc-9258-45e1-8a41-816bcd6f5ea3';
	
	+--------------------------------------+------------+-----------+------------+--------------+---------------+
	|             device_ID                | time_stamp | cpu_usage | disk_usage | memory_usage | network_usage |
	+--------------------------------------+------------+-----------+------------+--------------+---------------+
	| 4486d8dc-9258-45e1-8a41-816bcd6f5ea3 |  22:03:29  | 8         | 44         | 31           | 8             |
	+--------------------------------------+------------+-----------+------------+--------------+---------------+
```
----------------------------------------------------------------------------------------------------
Good reference articles:
- [Use JSON in MariaDB](https://mariadb.com/resources/blog/using-json-in-mariadb/)
- [How to Connect Python to MariaDB](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/)
- [MariaDB Administration](https://www.tutorialspoint.com/mariadb/mariadb_administration.htm)
- [List of JSON functions](https://mariadb.com/kb/en/json-functions/)
