def display_all_students(students):
    """Display details of all students."""

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        student.display_details()


def find_student_by_id(students, student_id):
    """Find and return a student using student ID."""

    for student in students:
        if student.student_id == student_id:
            return student

    return None