import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="school_db"
    )

    update = mydb.cursor()
    update.execute("update student set class = '6th' where id = 16")
    mydb.commit()
    print(f'{update.rowcount} user Updated.')
except Exception as e:
    mydb.rollback()
    print("Failed to Update User and Rolled backed Transaction")
    print("Error occurred:",e)
finally:
    update.close()
    mydb.close()
