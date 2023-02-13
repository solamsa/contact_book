import sqlite3

con = sqlite3.connect("contacts_database.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE contacts(name,number,email)")
except sqlite3.OperationalError:
    pass
