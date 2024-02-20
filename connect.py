import sqlite3
from contextlib import contextmanager

database = './tables.db'

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()


def read_sql_query(file_path):
    with open(file_path, 'r') as file:
        sql_query = file.read()
    return sql_query

def get_results_of_query(query):
    with create_connection(database) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        top_students = cursor.fetchall()
        return top_students
    

if __name__ == "__main__":
    file_path_1 = 'query_1.sql'
    query_1 = read_sql_query(file_path_1)

    file_path_2 = 'query_2.sql' 
    query_2 = read_sql_query(file_path_2)

    file_path_3 = 'query_3.sql' 
    query_3 = read_sql_query(file_path_3)

    file_path_4 = 'query_4.sql' 
    query_4 = read_sql_query(file_path_4)

    file_path_5 = 'query_5.sql' 
    query_5 = read_sql_query(file_path_5)

    file_path_6 = 'query_6.sql' 
    query_6 = read_sql_query(file_path_6)

    file_path_7 = 'query_7.sql' 
    query_7 = read_sql_query(file_path_7)

    file_path_8 = 'query_8.sql' 
    query_8 = read_sql_query(file_path_8)

    file_path_9 = 'query_9.sql' 
    query_9 = read_sql_query(file_path_9)

    file_path_10 = 'query_10.sql' 
    query_10 = read_sql_query(file_path_10)


top_students_1 = get_results_of_query(query_1)
print("\nQuery_1: Top 5 students with highest average grades:")
for student in top_students_1:
    print(f"Student ID: {student[0]}, Name: {student[1]}, Average Grade: {student[2]}")  
    
top_students_2 = get_results_of_query(query_2)
print("\nQuery_2: Student with the highest average grades with 'Optimized real-time paradigm':")
for student in top_students_2:
    print(f"Student ID: {student[0]}, Name: {student[1]}, Average Grade: {student[2]}")

top_students_3 = get_results_of_query(query_3)
print("\nQuery_3: Average grades for groups with 'Diverse uniform emulation':")
for student_group in top_students_3:
    print(f"Group: {student_group[0]}, Average Grade: {student_group}")

top_students_4 = get_results_of_query(query_4)
print("\nQuery_4: Average grades for groups:")
for student_group in top_students_4:
    print(f"Group: {student_group[0]}, Average Grade: {student_group}")

top_students_5 = get_results_of_query(query_5)  ###
print("\nQuery_5:Subjects of Laura Ryan:")
for subject in top_students_5:
    print(f"Subject: {subject}")

top_students_6 = get_results_of_query(query_6) 
print("\nQuery_6: List of students of group 2:")
for student in top_students_6:
    print(f"Student Name: {student}")  

top_students_7 = get_results_of_query(query_7) 
print("\nQuery_7: Students grades of group 2 with 'Public-key explicit conglomeration':")
for student in top_students_7:
    print(f"Student ID: {student[0]}, Name: {student[1]}, Grades: {student[2]}")   

top_students_8 = get_results_of_query(query_8) 
print("\nQuery_8: Average grade given by Kevin White in a the Assimilated holistic data-warehouse:")
print(top_students_8)

top_students_9 = get_results_of_query(query_9) 
print("\nQuery_9: Courses attended by the Paul Crane:")
for subject in top_students_9:
        print(f"Subject: {subject[0]}")


top_students_10 = get_results_of_query(query_9) 
print("\nQuery_10: Classes conducted by Kevin White for Ryan Rodriguez ")
for subject in top_students_10:
        print(f"Subject: {subject[0]}")
