import sqlite3 
conn =sqlite3.connect('shop.db')
cursor = conn.cursor()

query = """
CREATE TABLE test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quewn TEXT,
    ansver TEXT,
   
)

"""
cursor.execute(query)
conn.commit()
