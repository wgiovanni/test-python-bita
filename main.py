from config import (
    DATABASE_HOST,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME,
)
import psycopg2
conn = None

# DATABASE CONNECTION
try:
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        port=DATABASE_PORT,
        dbname=DATABASE_NAME
    )
except psycopg2.DatabaseError as e:
    print(e)

# TEST CONNECTION 
cursor = conn.cursor()
cursor.execute("SELECT * FROM stock")
data = cursor.fetchall()

print(data)

