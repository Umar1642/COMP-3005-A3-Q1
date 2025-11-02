import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="a3",
        user="postgres",
        password="Adt365*98rt!55"
    )

def getAllStudents():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()
    print("All Students:")
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def addStudent(first_name, last_name, email, enrollment_date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date)
    )
    connection.commit()
    print(f"Student {first_name} {last_name} added")
    cursor.close()
    connection.close()


def updateStudentEmail(student_id, new_email):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id)
    )
    if cursor.rowcount == 0:
        print("Error: No student found with that ID")
    else:
        connection.commit()
        print(f"Updated email for student ID {student_id}")
    cursor.close()
    connection.close()

def deleteStudent(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s;", 
        (student_id,)
    )
    if cursor.rowcount == 0:
        print("Error: No student found with that ID")
    else:
        connection.commit()
        print(f"Successfully deleted student with ID {student_id}")
    cursor.close()
    connection.close()

def main():
    getAllStudents()
    # addStudent("Ali", "Khan", "ali.khan@example.com", "2025-11-01")
    # updateStudentEmail(15, "jane.smith2@example.com")
    getAllStudents()
    deleteStudent(19)
main()