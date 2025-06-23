from Students import Student

# Create student objects
#print(student1.student_id)
student1 = Student("Ramu")
print(student1.student_id)
##print(student1.generate_stu_id())
student2 = Student("Balu")
#print(student2.generate_stu_id())
student3 = Student('Raju')
#print((student3.generate_stu_id()))
print(student2.student_id)
print(student3.student_id)


# Add grades to each student
#print(student1.student_id)
for grade in [85, 90, 78,90,80]:
    print(student1.add_grade(grade))

for grade in [100, 70, 100,49,60]:
    print(student2.add_grade(grade))

for grade in [90, 70, 40,49,60]:
    print(student3.add_grade(grade))


# Check if a specific grade is passing
#grade_to_check = 75
students = [student1, student2, student3]

# Updated method using explicit for loop
for student in students:
    print(f"\n{student.name}'s grades and status:")
    for grade,status in student.grades_status():
        print(f"Grade: {grade} - {status}")

    avg = student.get_average_grade()
    print(f"{student.name}'s average grade: {avg:.2f}")
    print(f"Is passing?: {'Yes' if Student.is_passing(avg) else 'No'}")

    #result = "Yes" if Student.is_passing(students) else "No"
    #print(f"Is {grade_to_check} a passing grade for {student.name}? {result}")

# Print each student’s average grade
print(f"{student1.name}'s average grade: {student1.get_average_grade():.2f}")
print(f"{student2.name}'s average grade: {student2.get_average_grade():.2f}")
print(f"{student3.name}'s average grade: {student3.get_average_grade():.2f}")

# Print the total number of students
print(f"Total number of students: {Student.get_total_students()}")
