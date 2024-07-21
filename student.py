class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
        print(f"Grade {grade} added for {subject}.")

    def calculate_average(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_overall_grade(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)
        print(f"Student: {self.name}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    student_name = input("Enter the student's name: ")
    student = Student(student_name)

    while True:
        print("\nGrade Tracking System")
        print("1. Add Grade")
        print("2. Display Overall Grade")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter the subject: ")
            try:
                grade = float(input("Enter the grade: "))
                if 0 <= grade <= 100:
                    student.add_grade(subject, grade)
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '2':
            student.display_overall_grade()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
