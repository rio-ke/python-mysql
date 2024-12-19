import mysql.connector
from mysql.connector import errorcode

# Database connection details
db_config = {
    'user': 'root',
    'password': 'my-secret-pw',  # Replace with your root password
    'host': '127.0.0.1',  # Assuming localhost, change if necessary
    'port': '3306',  # Default MySQL port
}

try:
    # Establish connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

    # Switch to the new database
    conn.database = 'mydatabase'

    # Create a new table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id INT AUTO_INCREMENT PRIMARY KEY, "
        "username VARCHAR(255) NOT NULL, "
        "password VARCHAR(255) NOT NULL)"
    )

    print("Database and table created successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    conn.close()
