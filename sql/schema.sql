CREATE DATABASE IF NOT EXISTS nnrg_attendance CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE nnrg_attendance;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(200) NOT NULL,
  role VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE students (
  roll_no VARCHAR(20) PRIMARY KEY,
  name VARCHAR(100),
  department VARCHAR(100),
  branch VARCHAR(20),
  year INT,
  section VARCHAR(5),
  academic_year VARCHAR(20),
  semester VARCHAR(20)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATE,
  roll_no VARCHAR(20),
  status VARCHAR(10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE attendance_summary (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATE,
  department VARCHAR(100),
  branch VARCHAR(20),
  year INT,
  section VARCHAR(5),
  academic_year VARCHAR(20),
  semester VARCHAR(20),
  subject VARCHAR(100),
  present INT,
  absent INT,
  status VARCHAR(20)  -- submitted / approved
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
