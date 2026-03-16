class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return f"Grade {grade} added"
        return "Invalid grade"
    
    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def display_info(self):
        avg = self.get_average()
        return f"Student: {self.name} (ID: {self.student_id})\nGrades: {self.grades}\nAverage: {avg:.2f}"

student1 = Student("Farhad", "BS(CS)2022-26-21")
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)
print(student1.display_info()) 
student2 = Student("Ali Ahmed", "BS(CS)2022-26-25")
student2.add_grade(90)
student2.add_grade(88)
print(student2.display_info())