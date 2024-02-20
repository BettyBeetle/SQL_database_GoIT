SELECT
    student_group.group_name,
    students.student_name,
    grades.grade
FROM
    student_group
JOIN
    students ON student_group.student_name = students.student_name
JOIN
    grades ON students.student_id = grades.student_id
JOIN
    subjects ON grades.subject_name = subjects.subject_name
WHERE
    student_group.group_name = '2'
    AND subjects.subject_name = 'Public-key explicit conglomeration';
