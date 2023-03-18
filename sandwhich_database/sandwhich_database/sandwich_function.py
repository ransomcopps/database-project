import sqlite3
database = './static/data/sandwhich_database.db'
#Name Bread Cheese Meat Sauce Toping Anything Creator

def add_sandwich(name, bread, cheese, meat, sauce, toping, anything, creator):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO sandwich_table(name, bread, cheese, meat, sauce, toping, anything, creator) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, bread, cheese, meat, sauce, toping, anything, creator))
    conn.commit()
    conn.close()

def update_sandwich(name, bread, cheese, meat, sauce, toping, anything, creator):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("UPDATE sandwich SET name = ?, bread = ?, cheese = ?, meat = ?, sauce = ?, toping = ?, anything = ?, creator = ? WHERE rowid = ?", (name, bread, cheese, meat, sauce, toping, anything, creator,))
    conn.commit()
    conn.close()

def delete_sandwich(rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("DELETE FROM sandwich_table WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def get_sandwich(rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM sandwichs WHERE rowid = ?", (rowid,))
    engineer = {}

    for row in result: 
        sandwich = {
            'name': row[0],
            'bread': row[1],
            'cheese': row[2],
            'meat': row[3],
            'sauce': row[4],
            'toping': row[5],
            'anything': row[6],
            'creator': row[7],
        }

    conn.close()
    return sandwich

def get_all_sandwich_table():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM sandwich_table")
    sandwich = []

    for row in result: 
        sandwich = {
            'name': row[0],
            'bread': row[1],
            'cheese': row[2],
            'meat': row[3],
            'sauce': row[4],
            'toping': row[5],
            'anything': row[6],
            'creator': row[7],
        }
      

    conn.close()
    return sandwich

