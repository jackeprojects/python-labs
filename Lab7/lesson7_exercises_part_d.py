# Part D, Collections of objects

# 1. Create 6 Student objects with name and score
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self): # Task 4: return pass or fail based on score
        if self.score >= 50:
            return "PASS"
        return "FAIL"

student_1 = Student("James", 72)
student_2 = Student("Maya", 97)
student_3 = Student("John", 36)
student_4 = Student("Cara", 65)
student_5 = Student("Herman", 23)
student_6 = Student("Joline", 2)


# 2. Store all Student objects in a list
students = [student_1, student_2, student_3, student_4, student_5, student_6]


# 3. Loop through the list and print each student's name and score
for student in students:
    print(student.name, student.score, sep=" | ")


# 4. Add a get_status() method that returns "PASS" or "FAIL" based on the score
# See Student class above, get_status() method returns pass or fail based on student score


# 5. Loop through the students again and print each student's name and status
for student in students:
    print(student.name, student.get_status(), sep=" | ")


# 6. Use a list comprehension to create a new list containing only students with a score of 70 or higher
high_score_students = [student for student in students if student.score >= 70]
for student in high_score_students:
    print(student.name, student.score, student.get_status(), sep=" | ")