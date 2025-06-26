class Student:
    def __init__(self, student_id: int, name: str, grade: str):
        self.id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Grade: {self.grade}"