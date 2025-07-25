import mysql.connector
import sys

# DB connection config
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'test_db'
}

# Establish connection
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print("Database connection failed:", err)
    sys.exit()

# CRUD functions
def insert_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("User added successfully.")

def view_users():
    cursor.execute("SELECT id,name,email FROM users")    #select * from users;
    users = cursor.fetchall()
    for user in users:
        print(user)

def update_user(user_id, name, email):
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
    conn.commit()
    print("User updated successfully.")

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    print("User deleted successfully.")

# Menu loop
def menu():
    while True:
        print("\n--- User Management Menu ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            insert_user(name, email)
        elif choice == '2':
            view_users()
        elif choice == '3':
            uid = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            update_user(uid, name, email)
        elif choice == '4':
            uid = int(input("Enter user ID to delete: "))
            delete_user(uid)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

# Run the menu
if __name__ == "__main__":
    menu()

    cursor.close()
    conn.close()
