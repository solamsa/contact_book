import sqlite3

def create_table():
    cur.execute("CREATE TABLE contacts(name,number,email)")

def insert_values(name,number,email):
    cur.execute(f"""
        INSERT INTO contacts VALUES
            ('{name}', '{number}' , '{email}')
    """)
    con.commit()
     
def view_values():
    res = cur.execute("SELECT email FROM contacts")
    print(res.fetchall())
     
if __name__ == "__main__":
    con = sqlite3.connect("contact_book.db")
    cur = con.cursor()
    try:
        create_table()
    except sqlite3.OperationalError:
        print("contact table exists")

    res = cur.execute("SELECT name FROM sqlite_master")
    print(res.fetchone())
    insert_values("solam","0606482037","s@gmail.com")
    view_values()