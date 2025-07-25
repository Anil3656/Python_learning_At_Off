import mysql.connector


mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database="school_db")

con = mydb.cursor()
con.execute("select * from student")
rows = con.fetchall()
#rows = con.fetchone()
#rows = con.fetchmany(10)
print(con.rowcount)
print(rows)
for row in rows:
    print(row)