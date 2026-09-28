# Student Management System using Python OOP

## 📌 Project Overview

This project is a simple **Student Management System** built using **Python Object-Oriented Programming (OOP)**.

The purpose of this project is to understand how classes and objects can be used to represent real-world entities such as students.

The project also demonstrates how Python applications can be organized using **packages and modules** instead of writing the entire program in a single Python file.

---

## 🎯 Objectives

This project demonstrates the following Python concepts:

- Classes
- Objects
- `__init__()` constructor
- Instance variables
- Instance methods
- Class variables
- Class methods
- Dictionaries
- Lists
- Loops
- Functions
- Packages
- Modules
- Imports

---

## 📁 Project Structure

```text
student_management_system/
│
├── main.py
├── README.md
│
└── student_management/
    │
    ├── __init__.py
    ├── student.py
    └── utils.py
```

### File Responsibilities

| File | Purpose |
|---|---|
| `main.py` | Main entry point of the application |
| `student_management/__init__.py` | Initializes the `student_management` package |
| `student_management/student.py` | Contains the `Student` class |
| `student_management/utils.py` | Contains helper functions for working with multiple students |
| `README.md` | Contains project documentation |

---

# 🧑‍🎓 Student Class

The `Student` class represents an individual student.

Each student contains the following attributes:

- Name
- Email
- Student ID
- Course
- Marks

Example:

```python
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
```

Here, `student1` is an **object** created from the `Student` class.

---

# 🏗️ Constructor

The `__init__()` method is the constructor of the `Student` class.

```python
def __init__(self, name, email, student_id, course, marks):
    self.name = name
    self.email = email
    self.student_id = student_id
    self.course = course
    self.marks = marks

    Student.total_students += 1
```

The constructor automatically executes whenever a new `Student` object is created.

For example:

```python
student1 = Student(...)
```

automatically calls the `__init__()` method.

---

# ⚙️ Instance Methods

Instance methods work with individual student objects.

The project contains the following instance methods:

### `display_details()`

Displays the student's information.

```python
student1.display_details()
```

It displays information such as:

```text
Student ID: STU101
Name: Aarav Sharma
Email: aarav@gmail.com
Course: Python Programming
Marks: {'Python': 85, 'SQL': 78, 'AI': 92}
Average Marks: 85.0
```

---

### `update_marks()`

Updates a student's marks for a particular subject.

Example:

```python
student1.update_marks("Python", 95)
```

This changes the Python mark from its existing value to `95`.

---

### `calculate_average()`

Calculates the average marks of a student.

The calculation is:

```text
Average = Total Marks / Number of Subjects
```

For example:

```text
Python = 85
SQL = 78
AI = 92

Total = 255
Number of subjects = 3

Average = 255 / 3
Average = 85
```

---

# 👥 Class Variable

The project uses a class variable:

```python
total_students = 0
```

Unlike instance variables such as `name` or `email`, the class variable belongs to the entire `Student` class.

Whenever a new student is created:

```python
Student.total_students += 1
```

increases the student count.

For example:

```text
Create student1
Total Students = 1

Create student2
Total Students = 2

Create student3
Total Students = 3
```

---

# 🏫 Class Method

The project contains the class method:

```python
@classmethod
def get_total_students(cls):
    return cls.total_students
```

It can be called using the class itself:

```python
Student.get_total_students()
```

Example output:

```text
Total Students: 3
```

---

# 🔍 Utility Functions

The `utils.py` module contains helper functions that work with multiple student objects.

### Display All Students

```python
display_all_students(students)
```

The function loops through the list of students and calls:

```python
student.display_details()
```

for every student.

---

### Find Student by ID

```python
find_student_by_id(students, "STU102")
```

The function searches through the student list.

If the student ID is found, the corresponding `Student` object is returned.

If the student is not found, the function returns:

```python
None
```

---

# 🔄 Program Flow

The program follows this sequence:

```text
Run main.py
     ↓
Import Student class
     ↓
Import utility functions
     ↓
Create Student objects
     ↓
__init__() executes for each object
     ↓
Student count increases
     ↓
Store Student objects in a list
     ↓
Display all students
     ↓
Calculate average marks
     ↓
Update student marks
     ↓
Display updated information
     ↓
Search for student using Student ID
     ↓
Display total number of students
     ↓
Program ends
```

---

# ▶️ How to Run the Project

Open the project folder in VS Code.

Make sure the terminal is opened at:

```text
student_management_system/
```

Run:

```bash
python main.py
```

---

# 💻 Sample Output

```text
========== ALL STUDENTS ==========

----- Student Details -----
Student ID: STU101
Name: Aarav Sharma
Email: aarav@gmail.com
Course: Python Programming
Marks: {'Python': 85, 'SQL': 78, 'AI': 92}
Average Marks: 85.0

----- Student Details -----
Student ID: STU102
Name: Diya Rao
Email: diya@gmail.com
Course: Data Science
Marks: {'Python': 90, 'SQL': 88, 'AI': 95}
Average Marks: 91.0

----- Student Details -----
Student ID: STU103
Name: Vikram Nair
Email: vikram@gmail.com
Course: Artificial Intelligence
Marks: {'Python': 75, 'SQL': 82, 'AI': 89}
Average Marks: 82.0

========== UPDATE MARKS ==========

Python marks updated successfully.

========== SEARCH STUDENT ==========

Student found!

========== STUDENT COUNT ==========

Total Students: 3
```

---

# 🧠 OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Class | `Student` |
| Objects | `student1`, `student2`, `student3` |
| Constructor | `__init__()` |
| Instance Attributes | `name`, `email`, `student_id`, `course`, `marks` |
| Instance Method | `display_details()` |
| Instance Method | `update_marks()` |
| Instance Method | `calculate_average()` |
| Class Variable | `total_students` |
| Class Method | `get_total_students()` |
| Package | `student_management` |
| Modules | `student.py`, `utils.py` |
| Package Initialization | `__init__.py` |

---

# 📚 Key Learning

This project demonstrates the difference between a **class** and an **object**.

A class acts as a blueprint:

```text
Student Class
      ↓
   Blueprint
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
S1   S2   S3
```

Each student object has its own information:

```text
student1 → Aarav
student2 → Diya
student3 → Vikram
```

However, the class variable:

```python
total_students
```

is shared at the class level and keeps track of how many student objects have been created.

Another important concept is:

```text
self → refers to the current object

cls → refers to the current class
```

---

## 🚀 Future Enhancements

The Student Management System can later be enhanced by adding:

- User input for student registration
- Marks validation
- Exception handling
- Custom exceptions
- Logging
- Delete student functionality
- Course management
- Grade calculation
- Pass/fail status
- File handling
- JSON or CSV storage
- Database integration
- Menu-driven interface

---

## ✅ Conclusion

This project provides a practical introduction to **Object-Oriented Programming in Python**.

Instead of keeping all logic in one file, the application uses **packages and modules** to organize the code into separate responsibilities.

It demonstrates how classes, objects, constructors, instance methods, class variables, and class methods can work together to build a small real-world application.
