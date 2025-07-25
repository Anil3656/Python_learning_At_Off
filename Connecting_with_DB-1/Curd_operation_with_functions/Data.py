from App import MySQLCRUD

if __name__ == "__main__":
    # Replace with your MySQL credentials
    db = MySQLCRUD(
        host="localhost",
        user="root",
        password="root",
        database="users"
    )

    #db.create_user("Alice", "alice@example.com")
    #db.create_user("Bob", "bob@example.com")

    #print("\nAll Users:")
    db.read_users()

    #db.update_user(name= 'Alice', new_email="Alice_new@example.com")

    #print("\nAfter Update:")
    #db.read_users()

    #db.delete_user(user_id=2)

    #print("\nAfter Deletion:")
    #db.read_users()

    #db.close_connection()
