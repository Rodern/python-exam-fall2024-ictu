import sqlite3

conn=sqlite3.connect('login.db')
conn.execute("INSERT INTO LOGIN (NAME,)")
query=(''' CREATE TABLE LOGIN
      ( NAME         TEXT        NOT NULL,
       PASSWORD     TEXT        NOT NULL);''')
conn.execute(query)
conn.close