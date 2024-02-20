SELECT
    subjects.subject_name
FROM
    subjects
JOIN
    grades ON subjects.subject_name = grades.subject_name
JOIN
    students ON grades.student_id = students.student_id
WHERE
    students.student_name = 'Paul Crane';
