-- Create a view need_meeting that lists students requiring a meeting
-- Filter: score < 80 AND (no last_meeting OR last_meeting > 1 month ago)
CREATE VIEW need_meeting AS
SELECT name
    FROM students
    WHERE score < 80
    AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
