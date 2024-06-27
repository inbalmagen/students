

from actions.crud import add_student, delete_student, edit_student, students_list
from actions.search import search_by_grade, search_by_name, search_contains, serch_grade_above_80
from storage.loadsave import read_file, save_file


def students_menu():
    students = read_file()
    while True:
        print ("please choose an option:  ")
        print ("1. Add student")
        print ("2. Edit student")
        print ("3. Delete student")
        print ("4. Search student by grade")
        print ("5. Search grade above 80")
        print ("6. Search by name")
        print ("7. Search contains")
        print ("8. List of all students")
        print ("x. Exit menu")
        choice = input("please enter your choice:  ")
        
        if choice == "1":           
            print("add student selected")
            add_student(students)
            save_file(students)
        elif choice == "2":
            print("edit student is selected")
            edit_student(students)
            save_file(students)
        elif choice == "3":
            print("delete student is selected")
            delete_student(students)
            save_file(students)
        elif choice == "4":
            search_by_grade(students)
        elif choice == "5":
            print("search score above 80 selected")
            serch_grade_above_80(students)
        elif choice == "6":
            print("search student by name selected")
            search_by_name(students)
        elif choice == "7":
            print("search student containing word selected")
            search_contains(students)
        elif choice == "8":
            print("list of all students selected")
            students_list(students)
        elif choice == "x":
            print("exit is choiceed")
            exit()