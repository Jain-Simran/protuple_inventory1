import sqlite3


def create_db():
    con = sqlite3.connect(database=r'protuple_inventory.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee(eid INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,name text NOT NULL,"
        "email text NOT NULL,gender text NOT NULL,contact text NOT NULL,dob text NOT NULL,doj text NOT NULL,"
        "pass text NOT NULL,utype text NOT NULL,address text NOT NULL,salary text NOT NULL)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,name text NOT NULL,"
        "contact text NOT NULL,desc text NOT NULL)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT"
                ",name text NOT NULL)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS product(pid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,Supplier text NOT NULL,"
        "Category text NOT NULL,name text NOT NULL,price text NOT NULL,qty text NOT NULL,status text NOT NULL)")
    con.commit()


create_db()