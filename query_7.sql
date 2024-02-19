SELECT
    student_group.student_name,
    grades.grade
FROM
    student_group
JOIN
    grades ON student_group.student_id = grades.student_id
JOIN
    subjects ON grades.subject_name = subjects.subject_name
WHERE
    student_group.group_name = '2'
    AND subjects.subject_name = 'Fundamental motivating parallelism';
