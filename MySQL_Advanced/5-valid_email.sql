-- Create a trigger that resets valid_email only when the email has been changed
-- The trigger acts on the users table before an update occurs
DELIMITER //
CREATE TRIGGER reset_email_validity_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
