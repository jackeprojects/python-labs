# Part E, Objects inside objects

class Student:
    def __init__(self, name):
        self.name = name


# 1. Create a teacher with a name
class Teacher:
    def __init__(self, name):
        self.name = name


# 2. Create a Course class with a course name and a teacher, the teacher should be a Teacher object
class Course:
    def __init__(self, name, teacher: Teacher):
        self.name = name
        self.teacher = teacher
        self.students = []  # Task: 5 added students list

    def add_student(self, student: Student):
        self.students.append(student)


# 3. Create a Teacher object and use it when creating a Course object
teacher_1 = Teacher("Mr. Smith")

course_1 = Course("Python Fundamentals", teacher_1)


# 4. Print the course name and the teacher's name through the Course object
print(course_1.name, course_1.teacher.name, sep=" | ")


# 5. Extend Course so that it also contains an initially empty list of Student objects
# See Course class above, added empty list, students, inside of constructor


# 6. Add an add_student() method and use it to add 3 Student objects to the course
# See Course class above, add_student() method appends a student to the course's student list
student_1 = Student("James")
student_2 = Student("Maya")
student_3 = Student("John")

course_1.add_student(student_1)
course_1.add_student(student_2)
course_1.add_student(student_3)


# 7. Loop through course.students and print the name of every student
for student in course_1.students:
    print(student.name)