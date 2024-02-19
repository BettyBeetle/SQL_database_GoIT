-- SELECT
--     lecturers.lecturer_id,
--     lecturers.lecturer_name,
-- FROM
--     subjects
-- JOIN
--     subjects ON lecturers.lecturer_id = subjects.lecturer_id 
-- GROUP BY
--     lecturers.lecturer_id;
SELECT
    subject_name
FROM
    subjects
WHERE
    lecturer_id = (SELECT lecturer_id FROM lecturers WHERE lecturer_name = 'Karen Lawson MD');
