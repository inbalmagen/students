Student Management System
This project is a simple command-line CRUD (Create, Read, Update, Delete) and search application for managing student records. The application allows users to add, edit, delete, and search for students based on various criteria. The data is stored in a JSON file.

Table of Contents
Installation
Usage
Project Structure
Modules
actions/crud.py
actions/search.py
storage/loadsave.py
menu/menu.py
Running the Application
Installation


Clone the repository:


Copy code:
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system


(Optional) Create and activate a virtual environment:

Copy code:
python -m venv venv
source venv/bin/activate 


Install dependencies:

Copy code:
pip install -r requirements.txt

Usage
To start the application, run the following command:


Copy code:
python app.py

Project Structure:

student-management-system/
│
├── actions/
│   ├── crud.py
│   └── search.py
│
├── storage/
│   └── loadsave.py
│
├── menu/
│   └── menu.py
│
├── app.py
├── data.json
└── README.md

Modules
actions/crud.py
Contains functions for CRUD operations on student records.

add_student(students): Adds a new student to the list.
edit_student(students): Edits an existing student's details.
delete_student(students): Deletes a student from the list.
students_list(students): Prints the list of all students.
actions/search.py
Contains functions for searching student records.

search_by_grade(students): Searches students by grade.
search_by_name(students): Searches students by name.
search_contains(students): Searches students whose details contain a specific substring.
serch_grade_above_80(students): Searches students with grades above 80.
storage/loadsave.py
Contains functions for loading and saving student data to and from a JSON file.

read_file(): Reads student data from a JSON file.
save_file(students): Saves student data to a JSON file.
menu/menu.py
Contains the main menu function that handles user interactions.

students_menu(): Displays the menu and handles user choices.
Running the Application
Ensure you have Python installed.
Clone the repository and navigate to the project directory.
Run the application:

Copy code:
python app.py

Follow the on-screen instructions to manage student records. The menu options allow you to add, edit, delete, and search for students, as well as list all students.


Please choose an option:
1. Add student
2. Edit student
3. Delete student
4. Search student by grade
5. Search grade above 80
6. Search by name
7. Search contains
8. List of all students
x. Exit menu
Choose the appropriate option by entering the corresponding number or 'x' to exit.