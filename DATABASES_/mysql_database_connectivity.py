import mysql.connector

def show_database():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password= "2401",
            database= "students"
        )

        mycursor = conn.cursor()

        sql = "SELECT * FROM students_info"

        mycursor.execute(sql)

        for db in mycursor:
            print(db)

        print("Database connected successfully.")

    except mysql.connector.connect as err:
        print("Error while connecting: ", err)

    finally:
        if conn in locals() and conn.is_connected():
            conn.close()
            print("Connection closed")
show_database()