class Student():
   def __init__(self,student_name,marks):
       self.student_name=student_name
       self.marks= marks
student1 = Student('Julius Wambugu',450)
student2 = Student('Goffrey Otieno',478)
student3 = Student('Angela Rose',456)
print(student1.student_name)
print(student2.student_name)
print(student3.student_name)
print(student1.marks)
print(student2.marks)
print(student3.marks)
print(f"My name is {student1.student_name} and I got {student1.marks} in my last exam. ")
print(f"My name is {student2.student_name} and I got {student2.marks} in my last exam. ")
print(f"My name is {student3.student_name} and I got {student3.marks} in my last exam. ")

