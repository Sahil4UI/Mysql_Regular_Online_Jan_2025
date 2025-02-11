create database demo3;
use demo3;
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    salary DECIMAL(10, 2)
);

INSERT INTO employees 
(first_name, last_name, email, hire_date, salary)
VALUES
('John', 'Doe', 'john.doe@example.com', '2021-03-10', 55000.00),
('Jane', 'Smith', 'jane.smith@example.com', '2022-07-22', 60000.00),
('Raj', 'Patel', 'raj.patel@example.com', '2020-11-15', 50000.00),
('Aisha', 'Khan', 'aisha.khan@example.com', '2019-05-30', 65000.00),
('Ali', 'Ahmed', 'ali.ahmed@example.com', '2023-01-15', 47000.00);

create index myIndex on employees(salary);
select * from employees where salary>55000;

-- Stored Procedure

-- 


DELIMITER $$
CREATE PROCEDURE getEmployeeByID(in emp_id INT)
BEGIN
	select * from employees where employee_id = emp_id;
END $$
DELIMITER ;

CALL getEmployeeByID(2);










