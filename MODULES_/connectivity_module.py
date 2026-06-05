import mysql.connector

def show():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "2401",
        database = "students"
    )

    mycursor = conn.cursor()

    show_table = "SELECT * FROM students_info;"
    mycursor.execute(show_table)

    for db in mycursor:
        print(db)

    user = input("Which query you want to perform? ")

    if user == "INSERT":
        id = input("Enter id: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")

        insert = """INSERT INTO students_info (id,name,age,city) 
        VALUES (%s,%s,%s,%s);"""
        
        values = (id,name,age,city)

        mycursor.execute(insert, values)

        conn.commit()

        mycursor.execute(show_table)
        for db in mycursor:
            print(db)
    
    elif user == "UPDATE":
        update_data = input("Which data you want to update? ")

        if update_data == "name":

            update_id = input("Enter id to update: ")

            new_name = input("Enter new name: ")
            update = """ UPDATE students_info 
            SET name =%s 
            WHERE id = %s ;
            """
            value = (new_name, update_id)

            mycursor.execute(update, value)


        elif update_data == "age":

            update_id = input("Enter id to update: ")

            new_age = input("Enter new age: ")
            update = """ UPDATE students_info 
            SET age =%s 
            WHERE id = %s;
            """
            value = (new_age,update_id)

            mycursor.execute(update, value)

        elif update_data == "city":

            update_id = input("Enter id to update: ")

            new_city = input("Enter new city: ")
            update = """ UPDATE students_info 
            SET city =%s 
            WHERE id = %s;
            """
            value = (new_city, update_id)

            mycursor.execute(update, value)
    
        conn.commit()

        mycursor.execute(show_table)
        for db in mycursor:
            print(db)
        

    elif user == "DELETE":

        delete_id = input("Which row id you want to delete? ")

        delete = """DELETE FROM students_info
        WHERE id = %s; """

        value = (delete_id,)
        mycursor.execute(delete, value)

        conn.commit()

        mycursor.execute(show_table)
        for db in mycursor:
            print(db)


show()