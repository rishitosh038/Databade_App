import sqlite3


# Connect to SQLite Database
def connect_db():
    conn = sqlite3.connect("student_database.db")
    return conn


# Create Table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT       
        )
    """)

    conn.commit()
    conn.close()
    print("Table created successfully")


# Insert Record
def insert_student(name, age, course):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()
    print("Student inserted successfully")


# Fetch Records
def fetch_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nStudent Record:")
    print("ID | Name | Age | Course")
    print("-" * 30)

    for row in records:
        print(row[0], "|", row[1], "|", row[2], "|", row[3])

    conn.close()


# Update Records
def update_student(student_id, new_course):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE student SET course = ? WHERE id = ?",
        (new_course, student_id)
    )

    conn.commit()
    conn.close()
    print("Student update successfully")


# Delete Record
def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()
    print("Student delete successfully")


# Menu System
def main():
    create_table()

    while True:
        print("\n=== STUDENT DATABASE MENU ===")
        print("1. Insert Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            insert_student(name, age, course)
        
        elif choice == "2":
            fetch_students()
        
        elif choice == "3":
            student_id = int(input("Enter Student ID to update: "))

        elif choice == "4":
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)
        
        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

        