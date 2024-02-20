SELECT
    students.student_id,
    students.student_name,
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM
    students
JOIN
    grades ON students.student_id = grades.student_id
WHERE
    grades.subject_name = 'Optimized real-time paradigm'
GROUP BY
    students.student_id,
    students.student_name
ORDER BY
    average_grade DESC
LIMIT 1;



