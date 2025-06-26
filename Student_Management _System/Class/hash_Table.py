from student import Student
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def insert(self, student: Student):
        index = self._hash(student.id)
        for i, s in enumerate(self.table[index]):
            if s.id == student.id:
                self.table[index][i] = student
                print(f"🔄 Student {student.id} updated.")
                return
        self.table[index].append(student)
        print(f"✅ Student {student.id} added.")

    def search(self, student_id: int):
        index = self._hash(student_id)
        for student in self.table[index]:
            if student.id == student_id:
                return student
        return None

    def delete(self, student_id: int):
        index = self._hash(student_id)
        for i, student in enumerate(self.table[index]):
            if student.id == student_id:
                deleted_name = student.name  # 👈 Save name before deletion
                del self.table[index][i]
                print(f"🗑️ Student {student_id} ({deleted_name}) deleted.")
                return deleted_name
        print("❌ Student not found.")
        return None

    def display(self):
        print("\n📋 All Students in Hash Table:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}:")
                for student in bucket:
                    print(f"  {student}")
