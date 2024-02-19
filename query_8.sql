SELECT
    subjects.subject_name,
    lecturers.lecturer_name,
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM
    grades
JOIN
    subjects ON grades.subject_name = subjects.subject_name
JOIN
    lecturers ON subjects.lecturer_id = lecturers.lecturer_id
GROUP BY
    subjects.subject_name,
    lecturers.lecturer_name;
