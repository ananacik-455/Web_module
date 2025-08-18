import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="x0_tcBDdiPIXcekoqf_m",
        database="students_db"# optional
    )

    cursor = mydb.cursor()
    cursor.execute("select * from students;")
    data = cursor.fetchall()

    print("Studends:")
    for student in data:
        print(student)

    age = 20
    cursor.execute("select * from students where age > %s", (age,)) # %s <=> ?
    print(cursor.fetchall())

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if "mydb" in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Connection closed.")




