import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE movie(title, year, score)")
except sqlite3.OperationalError as sql:
    print(sql)
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())