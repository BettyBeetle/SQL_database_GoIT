SELECT DISTINCT
    subjects.subject_name
FROM
    student_group
JOIN
    grades ON student_group.student_id = grades.student_id
JOIN
    subjects ON grades.subject_name = subjects.subject_name
WHERE
    student_group.student_name = 'Jake Aguilar';
