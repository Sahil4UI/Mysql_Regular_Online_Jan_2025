create database myDb;
use myDb;
create table students 
(
  id int auto_increment primary key,
  name varchar(50),
  address text,
  grade int ,
  course_id int);
  
-- text - char , varchar , text

describe students;
-- how to change type of a column 
alter table students modify column grade char(3);

insert into students (name ,address,grade,course_id) values
("Amir","Delhi","A+",101),
("Shivam","Delhi","A",102),
("Naveen","Delhi","B",103),
("Sahil","Delhi","C",104),
("Manish","Delhi","F",105),
("Amit","Delhi","A+",106);

-- how to fetch all data - comments 
select * from students;

select * from students where id=1;

-- fetch the data of students whose id is 1,3,4
select * from students where id in (1,3,4); 
-- fetching data based on a range
 select * from students where id between 1 and 4;
-- find the records of students whose name starting with A
select * from students where name like "a%"; 
-- find the records of students whose name ends with R
select * from students where name like "%r"; 
-- find the records of students whose name contains M
select * from students where name like "%m%";
-- find the record of all students whose name's 3rd character is i
select * from students where name like "__i%";

-- sorting in ascending / desc
select * from students order by grade desc;
-- aliasing 
select id as "roll no",name as "Students Name" from students;

create table employees 
(emp_id int primary key auto_increment,
e_name varchar(20),
e_doj date,
e_dept varchar(20),
e_salary int);

insert into employees (e_name,e_doj,e_dept,e_salary)
values 
("ravi","2020-05-05","IT",56000),
("Amit","2021-10-10","IT",76000),
("Suresh","2020-05-05","HR",96000),
("himanshu","2022-05-05","HR",86000),
("Rohan","2023-05-05","Sales",36000),
("Anish","2024-05-05","sales",46000),
("Anuj","2024-12-012","Sales",16000);


select * from employees where e_salary > 45000 and e_salary <80000;

select * from employees where e_salary = (select max(e_Salary) from employees);

select * from employees order by e_Salary desc limit 1;

select count(*) from employees;

-- find the no of employees in each department
select e_dept , count(*) as "Total Employees" from employees group by e_dept ;










 
