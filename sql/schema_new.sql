CREATE DATABASE IF NOT EXISTS nnrg_attendance CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE nnrg_attendance;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(200) NOT NULL,
  role VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  faculty_name VARCHAR(100),
  department VARCHAR(100),  -- e.g., Computer Science Engineering, Pharmacy, MBA
  branch VARCHAR(50),      -- e.g., CSE, ECE, AIML, DS, IT
  section VARCHAR(10),     -- e.g., A, B, C
  academic_year VARCHAR(20), -- e.g., 2023-2024
  semester VARCHAR(20),    -- e.g., 1 Year, 2 Semester
  subject VARCHAR(100),
  date DATE DEFAULT (CURRENT_DATE),
  present_count INT,
  absent_count INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;