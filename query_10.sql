SELECT DISTINCT
    subjects.subject_name
FROM
    subjects
JOIN
    lecturers ON subjects.lecturer_id = lecturers.lecturer_id
JOIN
    grades ON subjects.subject_name = grades.subject_name
JOIN
    student_group ON grades.student_id = student_group.student_id
WHERE
    lecturers.lecturer_name = 'Kevin White'
    AND student_group.student_name = 'Ryan Rodriguez';
