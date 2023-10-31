
CHECK_CREDENTIALS = '''SELECT user_id FROM authentication 
                        WHERE user_id = ? AND Password = ?'''

CHECK_ROLE = '''SELECT Designation FROM employee_details 
                WHERE user_id = ?'''

VIEW_DETAIL = '''SELECT * FROM employee_details 
                WHERE user_id = ?'''

CHANGE_PHONE = '''UPDATE employee_details 
                SET Phone = ? WHERE user_id = ?'''

CHANGE_PASSWORD = '''UPDATE authentication 
                    SET Password = ? WHERE user_id = ?'''

ADD_LEAVE = '''INSERT INTO leave(
                leave_id, 
                user_id, 
                start_date, 
                end_date, 
                status) 
                VALUES 
                (?, ?, ?, ?, ?)'''

ADD_ATTENDANCE = '''INSERT INTO attendance(
                    attendance_id, 
                    user_id, 
                    marked_at) 
                    VALUES 
                    (?, ?, ?)'''

IS_USER_EXIST = '''SELECT EXISTS(
                    SELECT 1 
                    FROM authentication 
                    WHERE 
                    user_id = ?)'''

VIEW_ATTENDANCE = '''SELECT employee_details.user_id, employee_details.Name 
                    FROM employee_details  
                    JOIN relationship 
                    ON employee_details.user_id = relationship.user_id  
                    WHERE manager_id = ? '''

GET_LEAVE_DETAILS = '''SELECT leave.user_id, leave.start_date, leave.end_date 
                    FROM leave 
                    JOIN relationship 
                    ON leave.user_id = relationship.user_id  
                    WHERE manager_id = ? '''

GET_LEAVES_REMAINING = '''SELECT no_of_leaves 
                        FROM employee_details 
                        WHERE user_id = ?'''

ENTER_LEAVE_STATUS = '''UPDATE leave 
                        SET status = ? 
                        WHERE 
                        user_id = ?'''

UPDATE_LEAVE = '''UPDATE employee_details 
                SET no_of_leaves = ? 
                WHERE user_id = ?'''

INSERT_AUTHENTICATION = '''INSERT INTO authentication(
                            user_id, 
                            Username, 
                            Password) 
                            VALUES 
                            (?, ?, ?)'''

INSERT_EMPLOYEE = '''INSERT INTO employee_details(
                    user_id, name, designation, phone, no_of_leaves) 
                    VALUES (?, ?, ?, ?, ?)'''

INSERT_RELATIONSHIP = '''INSERT INTO relationship(
                        unique_id, 
                        user_id, 
                        manager_id) 
                        VALUES 
                        (?, ?, ?)'''

DELETE_AUTHENTICATION = '''DELETE FROM authentication 
                            WHERE user_id = ?'''

DELETE_EMPLOYEE = '''DELETE FROM employee_details 
                    WHERE user_id = ?'''

DELETE_RELATIONSHIP = '''DELETE FROM relationship 
                        WHERE user_id = ?'''