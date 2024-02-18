SELECT
    student_group.group_name,
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM
    student_group
JOIN
    grades ON student_group.student_id = grades.student_id
WHERE
    grades.subject_name = 'Fundamental motivating parallelism'
GROUP BY
    student_group.group_name;
