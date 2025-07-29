import os
import sqlite3

def init_db():
    db_file = "workout_db.sqlite"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print(f"✅ Connected to {db_file}")

    # Check if table exists
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='users';
    """)
    result = cursor.fetchone()

    if result:
        print("✅ 'users' table already exists.")
    else:
        print("❌ 'users' table not found. Creating it...")
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                height REAL,
                weight REAL,
                fitness_level TEXT,
                activity_level TEXT,
                goal TEXT,
                workout_duration INTEGER,
                bmi REAL,
                calorie_target INTEGER
            )
        """)
        conn.commit()
        print("✅ 'users' table created successfully.")

    conn.close()


