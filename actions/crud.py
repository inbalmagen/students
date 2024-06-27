
from os import name


def add_student(students):
    new_student_name = input("enter student name: ")
    new_student_course = input("enter course: ")
    new_student_grade = int(input("enter student grade: "))
    new_student = {
        "name": new_student_name,
        "course": new_student_course,
        "grade": new_student_grade
    }
    students.append(new_student)

    print("student added")

def edit_student(students):
    name = input("Enter the name of the student to edit: ")
    for student in students:
        if student["name"] == name:
            new_name = input(f"Enter the new name (current: {student['name']}): ")
            new_grade = int(input(f"Enter the new grade (current: {student['grade']}): "))
            new_course = input(f"Enter the new course (current: {student['course']}): ")
            student["name"] = new_name
            student["grade"] = new_grade
            student["course"] = new_course
            print(f"student '{name}' updated successfully.")
            return
    print(f"student '{name}' not found.")


def delete_student(students):
    print("****** Deleting student ******")
    name = input("Please enter the name of the student to delete: ")
    found = False
    i = 0
    
    while i < len(students):
        if students[i]["name"] == name:
            del students[i]
            found = True
            print(f"student '{name}' deleted successfully.")
            break  
        i += 1
    
    if not found:
        print(f"student '{name}' not found.")


def students_list(students):
    print("list of all students:  ")
    if students:
        for student in students:
            print(f"Name: {student['name']}, grade: {student['grade']}, course: {student['course']}")
    else:
        print("No students available.")