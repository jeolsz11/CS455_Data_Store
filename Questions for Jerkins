When inserting values into tables on the CS server, it doesn't work. It gives an error.

```
MariaDB [(none)]> use monstore;
Database changed
MariaDB [monstore]> create table devices (metrics JSON);
Query OK, 0 rows affected (0.049 sec)

MariaDB [monstore]> create table error_log (error JSON, date varchar(10));
Query OK, 0 rows affected (0.058 sec)
MariaDB [monstore]> describe devices;
+---------+----------+------+-----+---------+-------+
| Field   | Type     | Null | Key | Default | Extra |
+---------+----------+------+-----+---------+-------+
| metrics | longtext | YES  |     | NULL    |       |
+---------+----------+------+-----+---------+-------+
1 row in set (0.021 sec)

MariaDB [monstore]> describe error_log;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| error | longtext    | YES  |     | NULL    |       |
| date  | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.026 sec)
MariaDB [monstore]> insert into devices() values('{"ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", Time Stamp": "22:03:29", "CPU: 8, "DISK": 44,"MEMORY": 31, "Network": 8}');
ERROR 4025 (23000): CONSTRAINT `devices.metrics` failed for `monstore`.`devices`
MariaDB [monstore]> insert into devices() values('{"ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", Time Stamp": "22:03:29", "CPU: 8, "DISK": 44,"MEMORY": 31, "Network": 8}');
ERROR 4025 (23000): CONSTRAINT `devices.metrics` failed for `monstore`.`devices`
```

However, when doing the exact same thing in XAMPP, it works just fine.

```
MariaDB [(none)]> use metrics;
Database changed
MariaDB [metrics]> describe devices;
+---------+----------+------+-----+---------+-------+
| Field   | Type     | Null | Key | Default | Extra |
+---------+----------+------+-----+---------+-------+
| metrics | longtext | YES  |     | NULL    |       |
+---------+----------+------+-----+---------+-------+
1 row in set (0.031 sec)

MariaDB [metrics]> describe error_log;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| error | longtext    | YES  |     | NULL    |       |
| date  | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.048 sec)
MariaDB [metrics]> INSERT INTO error_log() VALUES('{"Message": "meow", "Device": 45}','04.04.2022');
Query OK, 1 row affected (0.011 sec)

MariaDB [metrics]> select * from error_log;
+-----------------------------------+------------+
| error                             | date       |
+-----------------------------------+------------+
| {"Message": "meow", "Device": 45} | 04.04.2022 |
+-----------------------------------+------------+
1 row in set (0.001 sec)

MariaDB [metrics]> select * from devices;
+------------------------------------------------------------------------------------------------------------------------------+
| metrics                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------+
| { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 } |
+------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.001 sec)
```

Also is the mariadb library not installed on the cs server?

```
cs$ python engine_to_data_store.py
Traceback (most recent call last):
  File "engine_to_data_store.py", line 5, in <module>
    import mariadb
ModuleNotFoundError: No module named 'mariadb'
```
