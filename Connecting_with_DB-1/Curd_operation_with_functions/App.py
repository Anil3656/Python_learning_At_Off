import mysql.connector

class MySQLCRUD:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_user(self, name, email):
        sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
        values = (name, email)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(f"{self.cursor.rowcount} user added.")

    def read_users(self):
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_user(self, name, new_email):
        sql = "UPDATE user SET email = %s WHERE name = %s "
        values = (new_email, name)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(f"{self.cursor.rowcount} user updated.")

    def delete_user(self, user_id):
        sql = "DELETE FROM user WHERE id = %s"
        value = (user_id,)
        self.cursor.execute(sql, value)
        self.conn.commit()
        print(f"{self.cursor.rowcount} user deleted.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed.")

