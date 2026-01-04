CREATE DATABASE IF NOT EXISTS nnrg_attendance CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE nnrg_attendance;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  role ENUM('faculty','hod','dean','chairman','admin') NOT NULL,
  username VARCHAR(80) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE students (
  roll_no VARCHAR(30) PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  branch VARCHAR(50) NOT NULL,
  year SMALLINT NOT NULL,
  section VARCHAR(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  `date` DATE NOT NULL,
  roll_no VARCHAR(30) NOT NULL,
  status ENUM('present','absent') NOT NULL,
  faculty_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_attendance_date_roll (`date`, roll_no),
  FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE,
  FOREIGN KEY (faculty_id) REFERENCES users(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE attendance_summary (
  id INT AUTO_INCREMENT PRIMARY KEY,
  `date` DATE NOT NULL,
  branch VARCHAR(50) NOT NULL,
  year SMALLINT NOT NULL,
  section VARCHAR(10) NOT NULL,
  total_present INT NOT NULL,
  total_absent INT NOT NULL,
  status ENUM('submitted','pending','approved') DEFAULT 'submitted',
  faculty_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_summary_date_branch_year_section (`date`, branch, year, section),
  FOREIGN KEY (faculty_id) REFERENCES users(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
