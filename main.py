from config import (
    DATABASE_HOST,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME,
)
import psycopg2

#QUERIES
sql_delete = "DELETE FROM stock"

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

# DELETE DATA TABLE
cursor = conn.cursor()
cursor.execute(sql_delete)
conn.commit()


