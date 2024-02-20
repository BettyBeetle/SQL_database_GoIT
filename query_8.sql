SELECT
    subjects.subject_name,
    lecturers.lecturer_name,
    AVG(grades.grade) AS average_grade
FROM
    subjects
JOIN
    lecturers ON subjects.lecturer_id = lecturers.lecturer_id
JOIN
    grades ON subjects.subject_name = grades.subject_name
WHERE
    subjects.subject_name = 'Assimilated holistic data-warehouse' AND
    lecturers.lecturer_name = 'Kevin White'
GROUP BY
    subjects.subject_name, lecturers.lecturer_name;