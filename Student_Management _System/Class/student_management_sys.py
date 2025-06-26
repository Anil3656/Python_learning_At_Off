from student import Student
from hash_Table import HashTable
class StudentManagementSystem:
    def __init__(self):
        self.hash_table = HashTable()

    def run(self):
        while True:
            print("\n🎓 Student Management System")
            print("1. Add Student")
            print("2. Search Student")
            print("3. Delete Student")
            print("4. Display All Students")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                sid = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                grade = input("Enter Grade: ")
                student = Student(sid, name, grade)
                self.hash_table.insert(student)

            elif choice == '2':
                sid = int(input("Enter Student ID to search: "))
                student = self.hash_table.search(sid)
                if student:
                    print(f"🔍 Found: {student}")
                else:
                    print("❌ Student not found.")

            elif choice == '3':
                sid = int(input("Enter Student ID to delete: "))
                self.hash_table.delete(sid)

            elif choice == '4':
                self.hash_table.display()

            elif choice == '5':
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid choice. Try again.")