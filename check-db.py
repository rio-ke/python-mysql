import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.10",
  port=3310,
  user="ken",
  password="Ken@123"
)

print(mydb)
