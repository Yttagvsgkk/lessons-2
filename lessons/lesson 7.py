# CУБД Система упровления базы данных
# CRUD - Create, Read, Update, Delete

import  sqlite3



connect = sqlite3.connect('users.db')
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        fio VARCHAR (100), NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')