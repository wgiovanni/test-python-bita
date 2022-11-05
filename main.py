from config import (
    DATABASE_HOST,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME,
)
import psycopg2
import psycopg2.extras as extras
import time
import pandas as pd
import threading

# CONSTANTS
FILE_PATH = "Stock.CSV"
batchsize = 100000

#QUERIES
sql_insert = "INSERT INTO stock (point_of_sale, product, date, stock) VALUES (%s,%s,%s,%s)"
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

start_time = time.time()

# INSERRT DATA BATCH
def insert_data(sql, batc: list):
    with semaphore_insert:
        try:
            extras.execute_batch(cursor, sql, batc)
            conn.commit()
        except psycopg2.DatabaseError as e:
            print(e)
            conn.rollback()

    # READ FILE CSV
df = pd.read_csv(
    FILE_PATH, 
    sep = ';', 
    encoding='utf-8', 
    header=0,
    names=['point_of_sale', 'product', 'date', 'stock'],
    low_memory=False)

df['point_of_sale'] = df['point_of_sale'].astype('string')
df['product'] = df['product'].astype('string')
end = time.time() 
print("READ CSV: ",(end-start_time),"seg") 

# GET ROW IN TUPLE
data =  [tuple(x) for x in df.to_numpy()]

end = time.time() 
print("GET ROW IN TUPLE: ",(end-start_time),"seg") 

# BATCH LIST
batch = []
for i in range(0, len(data), batchsize):
    batch.append(data[i:i+batchsize])

end = time.time() 
print("BATCH LIST: ",(end-start_time),"seg") 

threads = []
# NUMBER OF THREADS
number_thread = int(len(data)/batchsize) + 1
semaphore_insert = threading.Semaphore(int(number_thread/4) + 1)

# ITERATE EACH THREAD 
for i in range(1, number_thread):
    t = threading.Thread(target=insert_data, args=(sql_insert,batch[i]))
    threads.append(t)
    t.start()
    t.join()

end = time.time() 
print("DONE: ",(end-start_time),"seg")

conn.close()

