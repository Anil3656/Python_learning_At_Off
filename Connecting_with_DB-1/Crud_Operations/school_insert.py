import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="school_db"
    )

    cursor = mydb.cursor()
    cursor.execute("insert into student(s_name,class,age) values('Anil', '5th' ,10)")
    #cursor.execute("insert into student(s_name,class,age) values('Rohan', None ,10)")
    #sql = "insert into student(s_name,class,age) values(%s,%s,%s)"
    #data = [("Amith",'4th',9), ("Rafi",'5th',10)]
    #cursor.executemany(sql, data)
    #cursor.execute(sql,(s_name,class,age))

    mydb.commit()

    print(f"{cursor.lastrowid} last Row Id")
    print(f'{cursor.rowcount} user added.')

    connected = mydb.is_connected()
    print(connected)
except Exception as e:
    mydb.rollback()
    print("Failed to add user. Rolled back transaction.")
    print("Error:", e)
finally:
    cursor.close()
    mydb.close()