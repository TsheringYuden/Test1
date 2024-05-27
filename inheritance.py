class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number
    
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

# Creating a Student object
student = Student("Alice", 20, "C123", "S456", "Computer Science", "Sophomore", 3.8)
print(f"Student Name: {student.name}")
print(f"Student Age: {student.age}")
print(f"Student CID: {student.cid_number}")
print(f"Student ID: {student.student_id}")
print(f"Student Course: {student.course}")
print(f"Student Year: {student.year}")
print(f"Student GPA: {student.gpa}")
student.walk()
student.talk()
student.eat()
student.sleep()
student.study()
student.attend_class()
student.write_exam()

# Creating a Teacher object
teacher = Teacher("Mr. Smith", 45, "T789", "Mathematics", 50000, "Science", "Professor")
print(f"\nTeacher Name: {teacher.name}")
print(f"Teacher Age: {teacher.age}")
print(f"Teacher CID: {teacher.cid_number}")
print(f"Teacher Subject: {teacher.subject}")
print(f"Teacher Salary: {teacher.salary}")
print(f"Teacher Department: {teacher.department}")
print(f"Teacher Designation: {teacher.designation}")
teacher.walk()
teacher.talk()
teacher.eat()
teacher.sleep()
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()
