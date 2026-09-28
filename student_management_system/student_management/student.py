class Student:
    """Represent a student in the Student Management System."""

    # Class variable
    total_students = 0

    def __init__(self, name, email, student_id, course, marks):
        """Initialize a new student."""

        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = marks

        Student.total_students += 1

    def display_details(self):
        """Display student information."""

        print("\n----- Student Details -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Average Marks:", round(self.calculate_average(), 2))

    def update_marks(self, subject, new_mark):
        """Update marks for a particular subject."""

        if subject in self.marks:
            self.marks[subject] = new_mark
            print(f"{subject} marks updated successfully.")
        else:
            print(f"{subject} is not found.")

    def calculate_average(self):
        """Calculate and return the student's average marks."""

        if not self.marks:
            return 0

        total = sum(self.marks.values())
        average = total / len(self.marks)

        return average

    @classmethod
    def get_total_students(cls):
        """Return the total number of student objects created."""

        return cls.total_students