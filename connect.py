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



top_students_1 = get_results_of_query(query_1)
print("\nTop 5 students with highest average grades:")
for student in top_students_1:
    print(f"Student ID: {student[0]}, Name: {student[1]}, Average Grade: {student[2]}")  
    
  
top_students_2 = get_results_of_query(query_2)
print("Student with the highest average grades with 'Fundamental motivating parallelism':")
for student in top_students_2:
    print(f"Student ID: {student[0]}, Name: {student[1]}, Average Grade: {student[2]}")


top_students_3 = get_results_of_query(query_3)
print("Average grades with 'Fundamental motivating parallelism:")
# for student in top_students_3:
#     print(f"Student ID: {student[0]}, Name: {student[1]}, Average Grade: {student[2]}")
print(top_students_3)