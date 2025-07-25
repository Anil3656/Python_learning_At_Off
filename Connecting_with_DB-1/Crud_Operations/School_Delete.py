import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="school_db"
    )

    delete = mydb.cursor()
    delete.execute("delete from student where id = 15")
    mydb.commit()
    #mydb.rollback()
    print(f'{delete.rowcount} user removed.')
except Exception as e:
    mydb.rollback()
    print("Failed to delete user and Rollback transaction!")
    print("Error Occurred:",e)
finally:
    delete.close()
    mydb.close()