import sqlite3

def connection():
    """function to connect to the database

    Returns:
        sqlite: connection to the database
    """
    con = sqlite3.connect("contacts_database.db")
    return con

def curs():
    """
        database curser
    Returns:
        sql: returns database curser
    """
    cur = connection().cursor()
    return cur

def details(name,number,email):
    
    curs().execute(f"""
    INSERT INTO contacts VALUES
        ('{name}', '{number}', '{email}')
""")
    connection().commit()

def view_details():
    res = curs().execute("SELECT name,number FROM contacts")
    a = res.fetchall()
    return a

if __name__ == "__main__":
    # name = input("Enter Name: ")
    # number = input("Input Number: ")
    # email = input("Input email")
    # details(name,number,email)
    print(view_details())