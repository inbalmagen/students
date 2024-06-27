
def search_by_grade(students):
    print("list of students with grade by choice: ")
    if students:
        grade_to_search = int(input("enter student grade to search: "))
        for student in students:
            if student['grade'] == grade_to_search:
                print(f"Name: {student['name']}, Grade: {student['grade']}, Course: {student['course']}")
    else:
        print("No students available.")

def search_by_name(students):
    if students:
        name_to_search = input("enter student name to search: ")
        for student in students:
            if student['name'] == name_to_search:
                 print(f"Name: {student['name']}, Grade: {student['grade']}, Course: {student['course']}")
    else:
        print("No students available.")

def search_contains(students):
    print("list of students: ")
    if students:
        name_to_search = input("enter search word: ").lower()
        for student in students:
            if name_to_search in student['name'].lower():
                 print(f"Name: {student['name']}, Grade: {student['grade']}, Course: {student['course']}")
    else:
        print("No students available.")


def serch_grade_above_80(students):
    print("list of students with grade above 80: ")
    if students:
        for student in students:
            if student['grade'] > 80 :
                 print(f"Name: {student['name']}, Grade: {student['grade']}, Course: {student['course']}")
    else:
        print("No students available.")
