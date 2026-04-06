import sqlite3

def connect():
    return sqlite3.connect("movies.db")

def setup():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("create table if not exists movies(name text unique, genre text)")
    cur.execute("create index if not exists idx_genre on movies(genre)")
    
    conn.commit()
    conn.close()

def add_movie():
    name = input("Enter movie name: ").strip()
    genre = input("Enter genre: ").strip()
    
    if not name or not genre:
        print("Invalid input")
        return
    
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert or ignore into movies values(?,?)", (name, genre))
    
    if cur.rowcount == 0:
        print("Movie already exists")
    else:
        print("Movie added")
    
    conn.commit()
    conn.close()

def view_movies():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from movies")
    rows = cur.fetchall()
    
    if not rows:
        print("No movies found")
    else:
        print("\nAll Movies:")
        for r in rows:
            print(f"{r[0]} - {r[1]}")
    
    conn.close()

def search_by_genre():
    g = input("Enter genre: ").strip()
    
    conn = connect()
    cur = conn.cursor()
    cur.execute("select name from movies where genre=?", (g,))
    res = cur.fetchall()
    
    if not res:
        print("No movies found")
    else:
        print("\nMatching Movies:")
        for i in res:
            print(i[0])
    
    conn.close()

def update_movie():
    name = input("Enter movie name to update: ").strip()
    new_genre = input("Enter new genre: ").strip()
    
    conn = connect()
    cur = conn.cursor()
    cur.execute("update movies set genre=? where name=?", (new_genre, name))
    
    if cur.rowcount == 0:
        print("Movie not found")
    else:
        print("Movie updated")
    
    conn.commit()
    conn.close()

def delete_movie():
    name = input("Enter movie name to delete: ").strip()
    
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from movies where name=?", (name,))
    
    if cur.rowcount == 0:
        print("Movie not found")
    else:
        print("Movie deleted")
    
    conn.commit()
    conn.close()

def sort_movies():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from movies order by name")
    rows = cur.fetchall()
    
    if not rows:
        print("No movies found")
    else:
        print("\nSorted Movies:")
        for r in rows:
            print(f"{r[0]} - {r[1]}")
    
    conn.close()

def count_by_genre():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select genre, count(*) from movies group by genre")
    rows = cur.fetchall()
    
    if not rows:
        print("No data")
    else:
        print("\nMovies Count by Genre:")
        for r in rows:
            print(f"{r[0]}: {r[1]}")
    
    conn.close()

def menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Sort 7.Count 8.Exit")
        ch = input("Enter choice: ")
        
        if ch == "1":
            add_movie()
        elif ch == "2":
            view_movies()
        elif ch == "3":
            search_by_genre()
        elif ch == "4":
            update_movie()
        elif ch == "5":
            delete_movie()
        elif ch == "6":
            sort_movies()
        elif ch == "7":
            count_by_genre()
        elif ch == "8":
            break
        else:
            print("Invalid choice")

setup()
menu()