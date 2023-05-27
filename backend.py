import sqlite3
def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id integer primary key,title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()
def insert (title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (null, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?",(title,author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("update book set title=?, author=?, year=?, isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()