import sqlite3

def create_table():
    cur.execute("""CREATE TABLE contacts(contactid INTEGER PRIMARY KEY AUTOINCREMENT,
   name,number,email)""")

def insert_values(name,number,email):
    # ID = 1
    cur.execute(f"""
        INSERT INTO contacts VALUES
            ('contactid','{name}', '{number}' , '{email}')
    """)
    con.commit()

    return 
     
def view_contacts(arg):
    res = cur.execute("SELECT name,number,email FROM contacts")
    for i in res.fetchall():
        print(i)

def delete(ID):
    cur.execute(f"""DELETE FROM contact_info WHERE ID""")
     
if __name__ != "__main__" :
    con = sqlite3.connect("contact_book.db")
    cur = con.cursor()
    try:
        create_table()
    except sqlite3.OperationalError:
        pass
        # print("contact table exists")

    # res = cur.execute("SELECT name FROM sqlite_master")
    # print(res.fetchone())
    # # insert_values("solam","0606482037","s@gmail.com")
    # view_values()