from datetime import datetime
import faker
import random
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_LECTURERS = 5
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20

def generate_fake_data(
    number_students, number_lecturers, number_groups, number_subjects, number_grades
):
    fake_students = []
    fake_lecturers = []
    fake_groups = []
    fake_subjects = []
    fake_data_for_grades = []
    
    fake_data = faker.Faker()


    for _ in range(random.randint(30, number_students + 1)):        # generowanie od 30 do NUMBER_STUDENTS imion studentów
        fake_students.append(fake_data.name())
        fake_groups.append(random.randint(1, number_groups))        # generowanie nazwy grupy dla każdego studenta
                  

    for _ in range(3, number_lecturers + 1):                       
        fake_lecturers.append(fake_data.name())                     # generowanie od 3 do NUMBER_LECTURERS imion wykładowców


    for _ in range(random.randint(5, number_subjects + 1)):
        fake_subjects.append(
            (
                fake_data.catch_phrase(),                               # generuje od 5 do NUMBER_SUBJECTS losowych przedmiotów
                random.choice(fake_lecturers),                          # wybiera losowego wykładowcę z fake_lecturers
            )
        )

    
    for student_id in range(1, len(fake_students) + 1):
        
        student_subjects = set()
        for _ in range(random.randint(15, 20)):                             # generuje od 15 do 20 ocen dla każdego studenta
            fake_grades =[]
            for subject in fake_subjects:
                subject_name = subject[0]

                if subject_name  not in student_subjects:
                    student_subjects.add(subject_name)
                    fake_grades.append(float(fake_data.random_int(2, 5))) 
                    grade_date = datetime(2023, 10, random.randint(1, 31)).date()   # generuje loswą datę z października 2023
                    fake_data_for_grades.append(                                    # przekazuje informacje związane z oceną
                        (
                            student_id,
                            fake_grades[-1],
                            grade_date,
                            subject_name,
                        )
                    )


    return (
        fake_students,
        fake_lecturers,
        fake_groups,
        fake_subjects,
        fake_data_for_grades,
    )


def insert_data_to_db(students, lecturers, student_group, subjects, grades):
    
    with sqlite3.connect("tables.db") as con:
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
            INSERT INTO student_group(student_name, group_name)
            VALUES (?, ?)
        """
        cur.executemany(sql_to_student_group, [(student, group_name) for student, group_name in zip(students, student_group)])



        sql_to_subjects = """
            INSERT INTO subjects(subject_name, lecturer_id)
            VALUES (?, ?)
        """
        cur.executemany(
            sql_to_subjects, [(subject[0], subject[1]) for subject in subjects]
         )

        
        sql_to_grades = """
            INSERT INTO grades(student_id, grade, grade_date, subject_name)
            VALUES (?, ?, ?, ?)
        """
        cur.executemany(sql_to_grades, grades)
        
        con.commit()


if __name__ == "__main__":
    students, lecturers, student_group, subjects, grades = generate_fake_data(
        NUMBER_STUDENTS, NUMBER_LECTURERS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_GRADES
    )


insert_data_to_db(students, lecturers, student_group, subjects, grades)
print(f"\nStudents: {students}\n")
print(f"Lecturers: {lecturers}\n")
print(f"Student_group: {student_group}\n")
print(f"Subjects: {subjects}\n")
print(f"Grades: {grades}")







