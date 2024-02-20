-- SELECT 
--     subjects.subject_name
-- FROM 
--     subjects
-- JOIN 
--     lecturers ON subjects.lecturer_id = lecturers.lecturer_id
-- WHERE 
--     lecturers.lecturer_name = 'Crystal Ramirez';


SELECT
    subject_name
FROM
    subjects
WHERE
    lecturer_id = 'Laura Ryan';