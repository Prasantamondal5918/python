# Student Grade Management System

students = []


# Calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# Add student
def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    math = float(input("Enter Mathematics marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))
    computer = float(input("Enter Computer marks: "))
    bengali = float(input("Enter Bengali marks: "))

    total = math + science + english + computer + bengali
    percentage = total / 5
    grade = calculate_grade(percentage)

    student = {
        "id": student_id,
        "name": name,
        "roll": roll,
        "math": math,
        "science": science,
        "english": english,
        "computer": computer,
        "bengali": bengali,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)


# Display all students
def display_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\n----------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Roll       :", student["roll"])
        print("Mathematics:", student["math"])
        print("Science    :", student["science"])
        print("English    :", student["english"])
        print("Computer   :", student["computer"])
        print("Bengali    :", student["bengali"])
        print("Total      :", student["total"])
        print("Percentage :", student["percentage"], "%")
        print("Grade      :", student["grade"])


# Search student
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Roll       :", student["roll"])
            print("Total      :", student["total"])
            print("Percentage :", student["percentage"], "%")
            print("Grade      :", student["grade"])
            return

    print("Student not found.")


# Delete student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main program
while True:

    print("\n================================")
    print(" STUDENT GRADE MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice! Please try again.")