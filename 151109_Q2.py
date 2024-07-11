class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to the class.")

    def display_students(self):
        if not self.students:
            print("No students in the class.")
        else:
            print("Students in the class:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                total_grade = sum(student.grades.values())
                num_subjects = len(student.grades)
                average_grade = total_grade / num_subjects
                print(f"{student.name}'s average grade: {average_grade:.2f}")
                return
        print(f"Student {student_name} not found in the class.")

    def get_class_average(self, subject):
        total_grade = 0
        num_students = 0
        for student in self.students:
            if subject in student.grades:
                total_grade += student.grades[subject]
                num_students += 1
        if num_students > 0:
            class_average = total_grade / num_students
            print(f"Class average for {subject}: {class_average:.2f}")
        else:
            print(f"No students have grades for the subject {subject}.")

# Example 
classroom = Classroom()

student1 = Student("Christian", {"Math": 85, "English": 92, "Science": 78})
student2 = Student("Jezebel ", {"Math": 90, "English": 88, "Biology": 85})
student3 = Student("Michael ", {"History": 75, "Geography": 82, "Art": 90})

classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)

classroom.display_students()
classroom.get_student_average("Christian")
classroom.get_class_average("Math")