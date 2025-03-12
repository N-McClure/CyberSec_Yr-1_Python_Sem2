import sqlite3

def create_connection():
    # Making the connection global so that is can be used in other functions:
    global conn
        
    try:
        # Create a connection to sqlite database:
        conn = sqlite3.connect('newdb.db') # The name of the database should be "newdb.db".
    except Exception as err:
        print(err)
    else:
        print(conn)
        print('Connection has been created succefully ...')
        my_cursor = conn.cursor()
        print('Cursor created...')

    

def create_cursor():
    global my_cursor
    my_cursor = conn.cursor()
    print('Cursor created ...')
    
def create_table():
    sql = 'create table if not exists Students (name varchar(50), sid int not null, campus varchar(50))'
    my_cursor.execute(sql)
    print('Table added to the database.')
    
def insert_student(name, sid, campus):
    sql = 'insert into Students values (?,?,?)'
    my_cursor.execute(sql, (name, sid, campus))
    conn.commit()
    print('Student added to the database.')
    
# Insert multiple records:
def insert_many():
    students = [('Bob Brown', 789012, 'South Campus'),
                ('Emily Davis', 345678, 'East Campus')]
    
    my_cursor.executemany('INSERT INTO Students VALUES (?,?,?)', students)
    conn.commit()
    print('Multiple students added to the database.')
    
def read_students():
    sql = 'SELECT * FROM Students'
    my_cursor.execute(sql)
    rows = my_cursor.fetchall()
    for row in rows:
        print(row)
    
def update_student(name, sid):
    campus = input("Enter campus location: ")
    sql = 'UPDATE Students SET name=?, sid=?, campus=? WHERE name=?'
    my_cursor.execute(sql, (name, sid, campus, name))
    conn.commit()
    print('Student updated in the database.')
    
def delete_student(name):
    sql = 'DELETE FROM Students WHERE name=?'
    my_cursor.execute(sql, (name,))
    conn.commit()
    print('Student deleted from the database.')
    
# Function to retreive data from the database for a specified student:
def get_student():
    name = input('Enter the name of the student: ')
    sql = 'SELECT * FROM Students WHERE name=?'
    my_cursor.execute(sql, (name,))
    row = my_cursor.fetchone()
    if row:
        print('Student:', row)
        
# Function to clear the database of all rows in the table:
def clear_table():
    sql = 'DELETE FROM Students'
    my_cursor.execute(sql)
    conn.commit()
    print('All students deleted from the database.')


if __name__ == '__main__':
    # Create connection
    create_connection()

    # Creater cursor
    create_cursor()
    
    # Create a table:
    create_table()

    # CRUD Operations:
    # === Student Insertions ===
    insert_student('John Doe', 123456, 'Main Campus')
    insert_student('Jane Smith', 678901, 'Central Campus')
    insert_student('Alice Johnson', 234567, 'North Campus')
    
    # === Insertion of Multiple students ===
    insert_many()
    
    # === Student Readings ===
    read_students()
    
    # === Student Updates ===
    update_student('John Doe', 123456)
    
    # === Student Deletions ===
    delete_student('Jane Smith')
    
    # === Student Readings after Deletion ===
    read_students()
    
    # === Specific Student Retrieval ===
    get_student()
    
    # === Clear All Students ===
    clear_table()  

    # === Student Readings after Deletion ===
    read_students()
    
# Note: The database is persistent and will retain all data even after the program has finished running.

    # Close connection
    conn.close()
    print('Connection closed ...')
