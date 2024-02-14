from datetime import datetime
import faker
import random
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_LECTURERS = 5
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20

def generate_fake_data(number_students, number_lecturers, number_groups, number_subjects, number_grades):
    fake_students = []
    fake_lecturers = []
    fake_groups = []
    fake_subjects = []
    fake_grades = []
    student_group = [("A",), ("B",), ("C",)]
    fake_data = faker.Faker()

   
    for _ in range(number_students):
        fake_students.append(fake_data.name())
        fake_groups.append(random.randint(1, number_groups))

    for _ in range(number_lecturers):
        fake_lecturers.append(fake_data.name())

    # for _ in range(number_groups):
    #     fake_groups.append(random.randint(1, 3))
      
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.catch_phrase())

    for _ in range(number_grades):
        fake_grades.append(fake_data.random_int(2,5))

    return fake_students, fake_lecturers, fake_groups, fake_subjects, fake_grades

########################################



#def insert_data_to_db(students, lecturers, student_group, subjects, grades):

    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()

        sql_to_students = """
            INSERT INTO students(student_name)
            VALUES (?)
        """
        cur.executemany(sql_to_students, [(student,) for student in students])

        sql_to_lecturers = """
            INSERT INTO lecturers(lecturer_name)
            VALUES (?)
        """
        cur.executemany(sql_to_lecturers, [(lecturer,) for lecturer in lecturers])

        sql_to_student_group = """
            INSERT INTO student_group(group_id)
            VALUES (?)
        """
        cur.executemany(sql_to_student_group, [(group_id,) for group_id in student_group])
   
      


        sql_to_subjects = """
            INSERT INTO subjects(subject_id)
            VALUES (?)
        """
        cur.executemany(sql_to_subjects, subjects)


        sql_to_grades = """
            INSERT INTO grades(grade)
            VALUES (?)
        """
        cur.executemany(sql_to_grades, [(grade,) for grade in grades])



        con.commit()

    


students, lecturers, student_group, subjects, grades = generate_fake_data(NUMBER_STUDENTS, NUMBER_LECTURERS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_GRADES)

# students, student_group, subjects, lecturers, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_LECTURERS, NUMBER_GRADES))
#insert_data_to_db(students, lecturers, student_group, subjects, grades)
print(students)
print(lecturers)
print(student_group)
print(subjects)
print(grades)
