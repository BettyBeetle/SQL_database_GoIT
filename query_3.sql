SELECT
    student_group.group_name,
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM
    student_group
JOIN
    students ON student_group.student_name = students.student_name
JOIN
    grades ON students.student_id = grades.student_id
JOIN
    subjects ON grades.subject_name = subjects.subject_name
WHERE
    subjects.subject_name = 'Diverse uniform emulation'
GROUP BY
    student_group.group_name;
