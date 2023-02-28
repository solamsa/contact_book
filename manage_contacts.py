import sqlite3
from rich.console import Console
from rich.table import Table

def create_table():
    cur.execute("""CREATE TABLE CONTACTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
   NAME    TEXT    NOT NULL,
   PHONE   TEXT    NOT NULL,
   EMAIL
   )""")

def insert_values(name,number,email):
    # ID = 1
    cur.execute(f"""
        INSERT INTO contacts (NAME,PHONE,EMAIL)
        VALUES ('{name}', '{number}' , '{email}')
    """)
    con.commit()

    return 
     
def view_contacts(arg):
    contact_table = Table(title='CONTACTS')
    contact_table.add_column("ID", justify="right", style="cyan")
    contact_table.add_column("NAME", style="magenta")
    contact_table.add_column("PHONE", style="green")
    contact_table.add_column("EMAIL", style="blue")
    res = cur.execute("SELECT ID, NAME,PHONE,EMAIL FROM CONTACTS")
    contents = res.fetchall()
    for info in contents:
        contact_table.add_row(str(info[0]),info[1],info[2],info[3])
    console = Console()
    console.print(contact_table)


def delete(ID):
    cur.execute(f"DELETE FROM CONTACTS WHERE ID ='{ID}'")
    con.commit()

def update(ID, field, update_content):
    cur.execute(f"UPDATE CONTACTS SET '{field.upper()}' = '{update_content}' WHERE ID ='{ID}'")
    con.commit()
     
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