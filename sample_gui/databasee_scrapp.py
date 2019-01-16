import sqlite3

database: sqlite3.Connection

TABLE_NAME="BOOK"
TABLE_ID="TABLE_ID"
BOOK_NAME="BOOK_NAME"
BOOK_PRICE="BOOK_PRICE"

def startDatabase():
    global database
    database=sqlite3.connect('books_scrap.db')
    print("database established")
    create_table()
    return database
def create_table():
    table_query="CREATE TABLE IF NOT EXISTS "+TABLE_NAME+" \
                 ("+TABLE_ID+" INTEGER PRIMARY KEY AUTOINCREMENT, "+BOOK_NAME+" TEXT, "+BOOK_PRICE+" TEXT); "
    database.execute(table_query)
    print("table created successfully")

def value_insert(name,price):
    insert=" INSERT INTO "+TABLE_NAME+"("+BOOK_NAME+" ,"+BOOK_PRICE+" )VALUES('"+name+"','"+price+"');  "
    database.execute(insert)
    database.commit()

def read_data():
    database=startDatabase()
    RETRIVE_DATA=" SELECT * FROM webscrapp;"
    data = database.execute(RETRIVE_DATA)
    return data
