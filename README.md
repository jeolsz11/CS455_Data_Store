# 455_Data_Store
Datastore component of the CS 455 Monitor Project.

Agents, Engine, and Data Store are daemons (a computer program that runs as a background process, rather than being under the direct control of an interactive user).

Only Dash has user interface


TO DO LIST
- Communication testing with Engine
- Communication testing with Dash
- update table to new entry format
    - Current:
    ```
    { "ID": "4486d8dc-9258-45e1-8a41-816bcd6f5ea3", "Time Stamp": "22:03:29", "CPU": 8, "DISK": 44, "MEMORY": 31, "NETWORK": 8 }
    ```
   - Update to:
    ```
    { "ID": "00ce9834-8453-4580-8082-4d2748c84e65", "Time Stamp": 1650469613, "CPU": 10, "DISK": 3, "MEMORY": 66, "NETWORK": { "BYTES SENT": 1554241536, "BYTES RECIEVED": 3376441344 } }
    ```
