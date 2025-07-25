#Using "argparse" module we can perform database Transactions with python
#argparse is a standard Python module used to parse arguments passed from the command line.
import argparse
import mysql.connector
import sys

# MySQL config
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'parse_db'
}

# Connect to MySQL
try:
    conn = mysql.connector.connect(**config)    # here (**kwargs) it takes N number of parameters
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print("MySQL Connection Error:", err)
    sys.exit()

# Set up argparse
parser = argparse.ArgumentParser(description='Manage MySQL People Database')

subparsers = parser.add_subparsers(dest='command', required=True)

# Insert command
insert_parser = subparsers.add_parser('insert', help='Insert a new record')
insert_parser.add_argument('--name', required=True, help='Person name')
insert_parser.add_argument('--age', required=True, type=int, help='Person age')

# Update command
update_parser = subparsers.add_parser('update', help='Update an existing record')
update_parser.add_argument('--id', required=True, type=int, help='Record ID')
update_parser.add_argument('--name', required=True, help='New name')
update_parser.add_argument('--age', required=True, type=int, help='New age')

# Delete command
delete_parser = subparsers.add_parser('delete', help='Delete a record')
delete_parser.add_argument('--id', required=True, type=int, help='Record ID to delete')

# Parse args
args = parser.parse_args()

# Logic based on command
if args.command == 'insert':
    cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", (args.name, args.age))
    conn.commit()
    print(f"Inserted: {args.name}, Age: {args.age}")

elif args.command == 'update':
    cursor.execute("UPDATE people SET name = %s, age = %s WHERE id = %s", (args.name, args.age, args.id))
    conn.commit()
    print(f"Updated ID {args.id} to Name: {args.name}, Age: {args.age}")

elif args.command == 'delete':
    cursor.execute("DELETE FROM people WHERE id = %s", (args.id,))
    conn.commit()
    print(f"Deleted record with ID: {args.id}")

# Cleanup
cursor.close()
conn.close()
