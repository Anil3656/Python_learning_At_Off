import sys   #sys is used to read command-line arguments
import mysql.connector  #allows connection to a MySQL database using Python.

#Connect to MySQl Server
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'test_db'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
except Exception as err:            #mysql.connector.Error
    print("Error connecting to MySQL:", err)
    sys.exit()

#Read command-line arguments
args = sys.argv   #getpot() #argparse
#print(args[0])   Note: Always the args[0] is always current python_script name.
if len(args) < 2:
    print("Usage:\n  insert name age\n  update id name age\n  delete id")
    sys.exit()

command = args[1].lower()

#Perform requested operation
if command == "insert":
    if len(args) != 4:
        print("Usage: insert name age")
    else:
        name = args[2]
        age = int(args[3])
        cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        print(f"Inserted {name}, age {age}")

elif command == "update":
    if len(args) != 5:
        print("Usage: update id name age")
    else:
        id = int(args[2])
        name = args[3]
        age = int(args[4])
        cursor.execute("UPDATE people SET name = %s, age = %s WHERE id = %s", (name, age, id))
        conn.commit()
        print(f"Updated ID {id} to {name}, age {age}")

elif command == "delete":
    if len(args) != 3:
        print("Usage: delete id")
    else:
        id = int(args[2])
        cursor.execute("DELETE FROM people WHERE id = %s", (id,))
        conn.commit()
        print(f"Deleted record with ID {id}")

else:
    print("Unknown command. Use: insert, update, delete")

# Step 7: Close the connection
cursor.close()
conn.close()
