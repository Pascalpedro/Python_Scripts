
"""Access a Database
Get employee record
Ask DBA which database to use
Import the right Python modules
Insantiate a control object
Build a connection string
Connect to the database
Run a query and process the results
Close the connection...."""


import pyodbc

CONNSTR = \
'DRIVER={SQL Server}; SERVER=mhknbn2kdz.database.windows.net;' \
'DATABASE=AdventureWorks2021;uid=sqlfamily;PWD=sqlf@mily'

def get_employees():
    connection = pyodbc.connect(CONNSTR)
    query = '''
        SELECT DISTINCT TOP 5 FirstName, LastName
        FROM Person.Person
        ORDER BY LastName, FirstName;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row.FirstName, row.LastName)
    connection.commit()
    connection.close()

get_employees()