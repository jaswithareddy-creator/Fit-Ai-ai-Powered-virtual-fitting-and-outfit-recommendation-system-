import sqlite3


DATABASE = "fitai.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            height REAL,

            shoulder REAL,

            chest REAL,

            waist REAL,

            hip REAL,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS outfits (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            category TEXT,

            color TEXT,

            size TEXT,

            price REAL
        )
    """)


    connection.commit()

    connection.close()


if __name__ == "__main__":

    create_database()

    print("FitAI database created successfully.")
