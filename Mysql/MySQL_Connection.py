import mysql.connector

def initialize_connection():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="sampledb"
        )
        print("Connection to MySQL database successful!")
        return connection
    except mysql.connector.Error as err:
        # In case of connection errors
        print("Error: {}".format(err))
        return None
