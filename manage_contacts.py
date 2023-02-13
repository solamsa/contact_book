import sqlite3

# con = sqlite3.connect("tutorial.db")
# # cur = con.cursor()
# # res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

def details(name,number,email):
    con = sqlite3.connect("contacts_database.db")
    cur = con.cursor()
    cur.execute(f"""
    INSERT INTO contacts VALUES
        ('{name}', '{number}', '{email}')
""")
    con.commit()
def view_details():
    con = sqlite3.connect("contacts_database.db")
    cur = con.cursor()
    res = cur.execute("SELECT name,number FROM contacts")
    a = res.fetchall()
    return a
if __name__ == "__main__":
    # name = input("Enter Name: ")
    # number = input("Input Number: ")
    # email = input("Input email")
    # details(name,number,email)
    print(view_details())