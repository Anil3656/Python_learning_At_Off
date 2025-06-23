#import uuid
#import random

class Student:
    # Class variable to track the total number of students
    total_students = 0
    #Class variable for every student_id
    last_assigned_id = 0

    def __init__(self, name):
        self.name = name
        Student.last_assigned_id += 1  # Increment when a new student is created
        self.student_id = f'{self.name} Id is: {Student.last_assigned_id}'  #Assiged Id to student_id
        self.grades = []
        Student.total_students += 1  # Increment when a new student is created

    #@staticmethod
    '''def generate_stu_id():
        #random_num = random.randint(1, 100)
        #return f'Student Id: {random_num}'
        return int (uuid.uuid4())
'''
    # Instance method to add a grade
    def add_grade(self, grade):
            self.grades.append(grade)
            return f"\nGrade {grade} added for {self.name}."

    # Instance method to calculate average grade
    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    # Class method to return total number of students
    @classmethod
    def get_total_students(cls):
        return cls.total_students

    # Static method to check if a grade is passing
    @staticmethod
    def is_passing(average_grade):
        return average_grade >= 75

    # Updated method using explicit for loop
    def grades_status(self):
        status_list = []
        for grade in self.grades:
            if grade >= 75:
                status_list.append((grade, "Pass"))
            else:
                status_list.append((grade, "Fail"))
        return status_list

'''    #Using List comprehension [expression for Iteration in Iterations if condition]
    def grades_status(self):
        return [(grade,"Pass" if grade >= 75 else  "Fail") for grade in self.grades]'''
