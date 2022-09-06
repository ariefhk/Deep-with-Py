import mysql.connector
# establishing the connection
conn = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1', database='pythonsql')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
    "INSERT INTO mahasiswa(id_mahasiswa, NISN, Nama, Jurusan)"
    "VALUES (%s, %s, %s, %s)"
)

data = (2, '20SA1138', 'Budi Susanto', 'Sistem Informasi')

try:
    # Executing the SQL command
    cursor.execute(insert_stmt, data)
    # Commit your changes in the database
    conn.commit()
except:
    # Rolling back in case of error
    conn.rollback()
print("Data inserted")

conn.close()
