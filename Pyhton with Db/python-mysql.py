import mysql.connector

conn = mysql.connector.connect(
  user='root',
  password='',
  host='127.0.0.1',
  database='pythonsql'
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE()")

data = cursor.fetchone()
print("Connection established to: ",data)
#Closing the connection
conn.close()
