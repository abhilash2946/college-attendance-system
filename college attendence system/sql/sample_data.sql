USE nnrg_attendance;

INSERT INTO users (name, role, username, password_hash) VALUES
('Admin User', 'admin', 'admin', '$pbkdf2-sha256$29000$examplehashreplace'); -- replace with real hash via create_admin.py

-- Example students
INSERT INTO students (roll_no, name, branch, year, section) VALUES
('R001', 'Alice Kumar', 'CSE', 1, 'A'),
('R002', 'Bob Sharma', 'CSE', 1, 'A'),
('R003', 'Chinmay Rao', 'CSE', 1, 'A');
