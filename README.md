# Database Operations Using SQLite (Python)

## Project Overview

This project demonstrates how to perform database operations using SQLite in Python.

The application:
- Connects to a SQLite database
- Creates tables programmatically
- Inserts records dynamically
- Fetches records using SELECT queries
- Updates existing records
- Deletes records
- Uses parameterized queries to prevent SQL injection
- Commits and closes connections properly
- Displays results in a clean format

This project helps understand backend data storage and CRUD operations.

---

## Tools Used

- Python 3.x
- sqlite3 module (built-in)
- DB Browser for SQLite (optional GUI tool)
- VS Code

No external libraries required.

---

## Project Structure

database_app.py  
student_database.db  
README.md  

---

## How to Run the Project

1. Open terminal in the project directory
2. Run:

python database_app.py

3. Use the menu to:
   - Insert student records
   - View all students
   - Update student course
   - Delete student record

The database file `student_database.db` will be created automatically.

---

## Database Schema

Table Name: students

Columns:

- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- name (TEXT, NOT NULL)
- age (INTEGER)
- course (TEXT)

---

## Features Implemented

✔ Database connection using sqlite3  
✔ Table creation with CREATE TABLE  
✔ INSERT operation  
✔ SELECT query with fetchall()  
✔ UPDATE operation  
✔ DELETE operation  
✔ Parameterized queries using ? placeholders  
✔ Commit and close connection properly  
✔ Menu-driven CLI application  

---

## SQL Injection Prevention

Parameterized query example:

cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    (name, age, course)
)

Using placeholders (?) prevents SQL injection attacks and ensures safe query execution.

---

## Example Output

=== STUDENT DATABASE MENU ===  
1. Insert Student  
2. View Students  
3. Update Student  
4. Delete Student  
5. Exit  

---

## Concepts Covered

- What is SQLite?
- CRUD operations (Create, Read, Update, Delete)
- SQL queries
- Primary keys and auto-increment
- Parameterized queries
- fetchall() vs fetchone()
- Database commit and connection handling

---

## Learning Outcome

After completing this task, you can:

- Perform database operations in Python
- Build backend storage systems
- Implement CRUD functionality
- Prevent SQL injection attacks
- Design simple database-driven applications

---
