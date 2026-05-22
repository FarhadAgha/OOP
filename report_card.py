import pandas as pd

class Student:
    """A simple Student class"""
    def __init__(self, name, math, english, science):
        self.name = name
        self.math = math
        self.english = english
        self.science = science
    
    def total(self):
        """Return total marks"""
        return self.math + self.english + self.science
    
    def average(self):
        """Return average marks"""
        return self.total() / 3
    
    def grade(self):
        """Return letter grade based on average"""
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def get_report(self):
        """Return a dictionary of student data"""
        return {
            'Name': self.name,
            'Math': self.math,
            'English': self.english,
            'Science': self.science,
            'Total': self.total(),
            'Average': round(self.average(), 2),
            'Grade': self.grade()
        }


class ReportCard:
    """Class to manage multiple students and generate reports"""
    
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        """Add a student object to the list"""
        self.students.append(student)
    
    def load_from_csv(self, filename):
        """Load student data from CSV file and create Student objects"""
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            student = Student(row['name'], row['math'], row['english'], row['science'])
            self.add_student(student)
        print(f"Loaded {len(self.students)} students from {filename}")
    
    def create_dataframe(self):
        """Create a pandas DataFrame from all student reports"""
        reports = [student.get_report() for student in self.students]
        return pd.DataFrame(reports)
    
    def show_report(self):
        """Display the full report card"""
        df = self.create_dataframe()
        print("\n" + "=" * 60)
        print("STUDENT REPORT CARD")
        print("=" * 60)
        print(df.to_string(index=False))
        print("=" * 60)
    
    def show_top_student(self):
        """Find and display the top student by average"""
        df = self.create_dataframe()
        top = df.loc[df['Average'].idxmax()]
        print(f"\n TOP STUDENT: {top['Name']} (Average: {top['Average']}%, Grade: {top['Grade']})")
    
    def show_summary(self):
        """Show class summary statistics"""
        df = self.create_dataframe()
        print("\nCLASS SUMMARY")
        print("-" * 30)
        print(f"Total Students: {len(df)}")
        print(f"Class Average: {df['Average'].mean():.2f}%")
        print(f"Highest Average: {df['Average'].max():.2f}%")
        print(f"Lowest Average: {df['Average'].min():.2f}%")
        print("\nGrade Distribution:")
        grade_counts = df['Grade'].value_counts().sort_index()
        for grade, count in grade_counts.items():
            print(f"  {grade}: {count} student(s)")


# ========== MAIN PROGRAM ==========
if __name__ == "__main__":
    school = ReportCard() 
    school.load_from_csv('students_data.csv')
    school.show_report()
    school.show_top_student()  
    school.show_summary()
    print("\n" + "=" * 60)
    print("ADDING A NEW STUDENT MANUALLY")
    new_student = Student("Hassan", 88, 92, 84)
    school.add_student(new_student)
    
    school.show_report()
