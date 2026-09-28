from student_management import Student
from student_management.utils import display_all_students, find_student_by_id


# Create multiple Student objects

student1 = Student(
    "Aarav Sharma",
    "aarav@gmail.com",
    "STU101",
    "Python Programming",
    {
        "Python": 85,
        "SQL": 78,
        "AI": 92
    }
)

student2 = Student(
    "Diya Rao",
    "diya@gmail.com",
    "STU102",
    "Data Science",
    {
        "Python": 90,
        "SQL": 88,
        "AI": 95
    }
)

student3 = Student(
    "Vikram Nair",
    "vikram@gmail.com",
    "STU103",
    "Artificial Intelligence",
    {
        "Python": 75,
        "SQL": 82,
        "AI": 89
    }
)


# Store all student objects inside a list

students = [student1, student2, student3]


# Display all students

display_all_students(students)


# Update marks

print("\n========== UPDATE MARKS ==========")

student1.update_marks("Python", 95)

print("\nUpdated Student Details:")
student1.display_details()


# Search student by ID

print("\n========== SEARCH STUDENT ==========")

student = find_student_by_id(students, "STU102")

if student:
    print("Student found!")
    student.display_details()
else:
    print("Student not found.")


# Display total students

print("\n========== STUDENT COUNT ==========")

print(
    "Total Students:",
    Student.get_total_students()
)