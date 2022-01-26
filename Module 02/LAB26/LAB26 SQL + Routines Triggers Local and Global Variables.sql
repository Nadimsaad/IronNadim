USE employees_mod;

#Q2 create a procedure that provides the average salary of all employees#
DELIMITER $$
CREATE PROCEDURE avg_salary()
BEGIN
SELECT AVG(salary) 
     FROM t_salaries;
END$$
DELIMITER ;

#Q3 create a procedure called ‘emp_info’ that uses as parameters 1st+last name returning emp numb#
DELIMITER $$
CREATE PROCEDURE emp_info()
BEGIN
SELECT emp_no, first_name, last_name 
FROM t_employees ORDER BY department;

#Q5 create a function called ‘emp_info’ that takes for parameters the 1st+last name returning salary 
# from the newest contract of that employee. 
# Hint: In the BEGIN-END block of this prog, declare 2 var – v_max_from_date and v_salary#

DELIMITER $$

DROP FUNCTION emp_info$$

CREATE FUNCTION emp_info(p_first_name varchar(14), p_last_name varchar(14))

RETURNS DECIMAL (10,2)

DETERMINISTIC

BEGIN 
	DECLARE v_max_from_date date;
    DECLARE v_salary DECIMAL (10,2);
    
    SELECT MAX(from_date)
	INTO v_max_from_date 
    FROM t_employees e
    JOIN t_salaries s 
    ON e.emp_no = s.emp_no
	WHERE e.first_name = p_first_name
    AND e.last_name = p_last_name;
	
    SELECT MAX(salary)
    INTO v_salary
    FROM t_salaries s
    LEFT JOIN t_employees e
    ON e.emp_no = s.emp_no
    WHERE first_name = e.first_name
    AND last_name = e.last_name
    AND s.from_date = v_max_from_date;
	RETURN v_salary;
END $$

DELIMITER ;

## Q6 Create a trigger that checks if the hire date of an employee is higher than the current date. 
# If true, set this date to be the current date. Format the output appropriately (YY-MM-DD)

DELIMITER $$

CREATE TRIGGER date_check
BEFORE INSERT ON t_employees
FOR EACH ROW

BEGIN
	IF NEW.hire_date > current_date() THEN SET NEW.hire_date = current_date();
    END IF;
END $$

DELIMITER ;

# Q7 Create ‘i_hire_date’ and Drop the ‘i_hire_date’ index

CREATE INDEX test
ON t_employees(hire_date);

DROP INDEX test

ON t_employees;

# Q8 Select all records from the ‘salaries’ table of people whose salary is higher than $89,000 per annum. 
# Then, create an index on the ‘salary’ column of that table, 
# and check if it has speed up the search of the same SELECT statement

SELECT salary
FROM t_salaries
WHERE salary > 89000;

CREATE INDEX index_sal
ON t_salaries(salary);

# Q9 Use Case statement and obtain a result set containing the employee number, first name, 
# and last name of all employees with a number higher than 109990. Create a fourth column in the query, 
# indicating whether this employee is also a manager, according to the data provided in the dept_manager 
# table, or a regular employee.

SELECT e.emp_no, e.first_name, e.last_name, 
CASE
	WHEN e.emp_no = m.emp_no THEN "Yes"
    ELSE "No"
END AS Manager
FROM t_employees e
JOIN t_dept_manager m
ON m.emp_no = e.emp_no
WHERE e.emp_no > 109990
GROUP BY emp_no;

## Q10 Extract a dataset containing the following information about the managers: employee number, 
# first name, and last name. Add two columns at the end – one showing the difference between the 
# maximum and minimum salary of that employee, and another one saying whether this salary raise was 
# higher than $30,000 or NOT. 

# Q11 Extract the employee number, first name, and last name of the first 100 employees, and add a fourth 
# column, called “current_employee” saying “Is still employed” if the employee is still working in the 
# company, or “Not an employee anymore” if they aren’t. Hint: You’ll need to use data from both the 
# ‘employees’ and the ‘dept_emp’ table to solve this exercise.

SELECT r.emp_no, r.first_name, r.last_name,
CASE
	WHEN d.to_date < current_date() THEN "Not an employee anymore"
    ELSE "Is still employed"
END AS "current_employee"

FROM manager_raise r
JOIN t_dept_emp d
ON d.emp_no = r.emp_no
GROUP BY r.emp_no
ORDER BY r.emp_no
LIMIT 100;