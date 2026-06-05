import mysql.connector
import csv

def table():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "2401",
        database = "employees"
    )
    mycursor = conn.cursor()
    print("Your database is connected successfully.")

    delete = "DELETE FROM employee_data"
    mycursor.execute(delete)
    conn.commit()

    # create = """
    # CREATE TABLE employee_data (
    #     ID INT PRIMARY KEY,
    #     Name VARCHAR(50),
    #     Field VARCHAR(50),
    #     Salary INT
    #     )
    # """
    # mycursor.execute(create)
    # print("Table created")

    with open ("DSA/employees_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)


        for row in reader:
            id,name,field,salary = row

            insert = """
            INSERT INTO employee_data(ID,Name,Field,Salary) VALUES(%s,%s,%s,%s);
            """

            values = (int(id),name,field,int(salary))
            mycursor.execute(insert, values)
        
        conn.commit()

        print("Data inserted successfully!")

    # def sort_data():
    #     n = len(id) 
    #     for i in range(n):
    #         for j in range(i+1, n):

    #             if id[j] < id[i]:
    #                 id[i], id[j] = id[j],id[i]
    # sort_data()


    def final_data():

        show = "SELECT * FROM employee_data ORDER BY ID ASC;"
        mycursor.execute(show)
        for db in mycursor:
            print(db)
        
    final_data()
    

    search_data = input("Enter Data to search: ")

    search_query = """
        SELECT * FROM employee_data
        WHERE Name = %s OR ID = %s OR Field = %s OR Salary = %s
        """
    mycursor.execute(search_query, (search_data,search_data,search_data,search_data))
    result = mycursor.fetchall()

    if result:
        for row in result:
            print(row)
    else: 
        print("Data not Found!")
    
table()
