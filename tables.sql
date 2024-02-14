-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: lecturers
DROP TABLE IF EXISTS lecturers;
CREATE TABLE lecturers (
    lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecturer_name VARCHAR(255) UNIQUE NOT NULL

);
-- Table: student_group
DROP TABLE IF EXISTS student_group;
CREATE TABLE student_group (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name INTEGER,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);


-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(100) UNIQUE NOT NULL,
    lecturer_id INTEGER,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers(lecturer_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    grade FLOAT,
    grade_date DATE NOT NULL,
    subject_name VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (subject_name) REFERENCES subjects(subject_name)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
