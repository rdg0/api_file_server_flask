import sqlite3


def start_db():
    try:
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS file(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            extension TEXT,
            size REAL NOT NULL,
            hash TEXT
        );
        ''')
        con.commit()
        
    except Exception as error:
        print('Db not ok :(', error)
    finally:
        con.close()

def get_file(filename):
    """Получить файл по имени."""

    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file
        WHERE name = ?;
        ''', (filename,))
        
    return cur



def get_file_list():
    """Получаем из БД список всех файлов."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file;
        ''')
    return cur


def get_file_list_by_extension(extension):
    """Получаем из БД все файлы с определенным расширением."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute('''
        SELECT * FROM file
        WHERE extension = ?;
        ''', (extension,))
        
    return cur


def create_file(filename, extention, size, hash):
    """Добавляем в БД новый файл."""
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO file
        VALUES(NULL, ?, ?, ?, ?);
        """, (filename, extention, size, hash)
        )
    return cur


def delete_file(filename):
    """ Удаляем файл. """
    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.execute("""
        DELETE FROM file
        WHERE name = ?;""", (filename,)
        )
    return cur


##################################

start_db()
# create_file('test.txt', 'txt', 2.3, 'lkjdfkl')
# create_file('test_2.jpg', 'jpg', 4.8, 'jslsdhguisdfgui')
# create_file('test_3.doc', 'doc', 1.1, 'wierupdfgkjhasdfhu')
# create_file('test_4.jpg', 'jpg', 3.3, 'jklasdfhhiuhuohorpuyt')
# create_file('test_5.jpg', 'jpg', 4.9, 'iougghjgkfthbnt')

# delete_file('test.txt')

# files = get_file_list_by_extension('jpg')
# file = get_file('test_2.jpg')
# print(file.fetchall())


